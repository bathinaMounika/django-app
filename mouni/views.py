from django.shortcuts import render, redirect
from .models import (
    Exam, 
    Message, 
    Question,
    ResultPerExam,
)
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ExamModelForm, QuestionFormset
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import csv
import random

def get_remarks(percent):
    if percent > 90:
        return "Very Good"
    elif percent > 70:
        return "Good"
    elif percent > 40:
        return "Average"
    else:
        return "Poor"


class ExamListView(ListView):
    model = Exam
    template_name = 'mouni/home.html'
    context_object_name = 'exams'
    ordering = ['start'] 	



class ExamDetailView(LoginRequiredMixin, DetailView, UserPassesTestMixin):
    model = Exam #context_object_name = 'exam'
    ordering = ['-start']

    # def __init__(self, *args, **kwargs):
    #     super(ExamDetailView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ExamDetailView, self).get_context_data(**kwargs)
        try:
            r = ResultPerExam.objects.get(student_id = self.request.user.id, exam_id = self.kwargs[self.pk_url_kwarg])
            seed = r.seed
            print("seed read from ResultPerExam is ", seed)
            random.seed(seed)
            print("student already writen exam with seed = ", seed)
            context["has_written"] = True
            op_list = {}
            print(r.que_pick_ans)
            for _ in r.que_pick_ans.strip().split(","):
                print("_", _)
                qid, op_num, is_correct = [int(t) for t in _.strip().split(":")]
                print(qid, op_num)
                op_list[qid] = op_num
            context["op_list"] = op_list
        except ResultPerExam.DoesNotExist:
            context["has_written"] = False
            seed = random.randint(1, 100)
            random.seed(seed)
            context["seed"] = seed
            print("student now writing the exam with seed = ", seed)
        return context

    def post(self, request, *args, **kwargs):
        eid = request.POST['exam']
        seed = request.POST.get("seed")
        exam = Exam.objects.get(id = eid)
        res = exam.subject + " " + exam.skillType + " exam done!"
        res += "\n"
        res += "<h1>You have scored "
        score = 0
        print(exam.subject, exam.skillType)
        result = ResultPerExam()
        result.student_id = request.user.id
        result.exam_id = eid
        TM = result.total_marks = exam.question_set.count()
        result.que_pick_ans = ""
        for q in exam.question_set.all():
            print(q, q.ans, request.POST.get(str(q.id)))
            op, op_num = request.POST.get(str(q.id)).split("+")
            if q.ans == op:
                score += 1
                result.que_pick_ans += str(q.id) + ":" + op_num + ":1,"
            else:
                result.que_pick_ans += str(q.id) + ":" + op_num + ":0,"
        result.que_pick_ans = result.que_pick_ans.rstrip(",")
        result.marks = score
        percentage = (score/TM) * 100
        result.remarks = get_remarks(percentage)
        print("saving seed = ", seed)
        result.seed = seed
        result.save()
        res += str(score) + "</h1>"
        with open('results.csv', mode='a+', newline='') as f:
            fwriter = csv.writer(f, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
            fwriter.writerow([str(result.student_id), request.user, eid, exam.skillType, score, TM, percentage])
        f.close()

        #return HttpResponse(res, content_type="text/html")
        return redirect("mouni:display-results")



@login_required
def display_results(request):
    if request.method == 'GET':
        student_id = request.user.id
        context = {
            'results' : ResultPerExam.objects.filter(student_id = student_id)
        }
        return render(request, 'mouni/display-results.html', context)

class ResultDetailView(LoginRequiredMixin, DetailView):
    model = Exam
    template_name = 'mouni/result.html'
        


@login_required
@permission_required('mouni.add_exam', raise_exception=True)
def create_exam(request):
    template_name = 'mouni/create_exam.html'
    if request.method == 'GET':
        examform = ExamModelForm(request.GET or None, initial = {'teacher': request.user.username})
        examform.teacher = request.user.username
        formset = QuestionFormset(queryset=Question.objects.none())
    elif request.method == 'POST':
        examform = ExamModelForm(request.POST)
        formset = QuestionFormset(request.POST)
        if examform.is_valid() and formset.is_valid():
            # first save this exam, as its reference will be used in `Question`
            examform.teacher = request.user.username
            exam = examform.save()
            for form in formset:
                # so that `question` instance can be attached.
                question = form.save(commit=False)
                question.exam = exam 
                question.save()
            return redirect("mouni:exam-list")
    return render(request, template_name, {
        'examform': examform,
        'formset': formset,
    })

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['title', 'msg']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Message
    fields = ['title', 'msg']

    def form_valid(self, form):
        form.instance.student = self.request.user
        return super().form_valid(form)

    def test_func(self):
        msg = self.get_object()
        if self.request.user == msg.student:
            return True
        return False

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    success_url = '/'
    
    def test_func(self):
        msg = self.get_object()
        if self.request.user == msg.student:
            return True
        return False

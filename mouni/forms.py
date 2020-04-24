from django import forms
from django.forms import (formset_factory, modelformset_factory)
from .models import Exam, Question
from django.utils.translation import gettext_lazy as _

QuestionFormset = modelformset_factory(
    Question,
    fields=('question', 'ans', 'op2', 'op3', 'op4'),
    labels={'ans':'Answer', 'op2':'Option2', 'op3':'Option3', 'op4':'Option4'},
    extra=0,
    min_num = 1,
    validate_min = True,
    widgets={'question': forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Question here',
            'rows': "3"
        }),
    'ans': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter answer here',
        'label': "Answer"
        }),
    'op2': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter option2 here'
        }),
    'op3': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter option3 here'
        }),
    'op4': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter option4 here'
        }),
    }
)

class ExamModelForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'
        localized_fields = ['skillType', 'subject']
        readonly_fields = ['teacher']
        widgets = {
            'teacher': forms.TextInput(attrs={'readonly':'readonly'}),
            'subject': forms.TextInput(),
            'start': forms.DateTimeInput()
        }
        labels = {
            'skillType': _('Skill Type')
        }
        error_messages = {
            'subject': {
                'required': _("Enter subject"),
                'max_length': _("20 characters max"),
            },
            'skillType': {
                'required': _("Please enter skill"), 
                'max_length': _("20 characters max"),            
            },
            'start': {
                'required': _("Required exam start date and time"),
                'invalid': _("enter valid date and time"),
            },

        }

    def __init__(self, *args, **kwargs):
        super(ExamModelForm, self).__init__(*args, **kwargs)
        self.fields['subject'].error_messages = {'required': 'enter subject'}

   
        


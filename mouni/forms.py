from django import forms
from django.forms import (formset_factory, modelformset_factory)
from .models import Exam, Question

QuestionFormset = modelformset_factory(
    Question,
    fields=('question', 'ans', 'op2', 'op3', 'op4'),
    extra=1,
    widgets={'question': forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Question here'
        }),
    'ans': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter answer here'
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
        readonly_fields = ['teacher']
        widgets = {
            'teacher': forms.TextInput(attrs={'readonly':'readonly'})
        }
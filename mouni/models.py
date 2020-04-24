from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from random import shuffle
import random
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_fields(value):
	if not value.isalnum():
		raise ValidationError(_('%(value)s is not valid. Please use alphanumneric characters as subject names'), params={'value': value},)

class Exam(models.Model):
	skillType = models.CharField(max_length = 20, validators = [validate_fields], help_text = "skill you wanna test students in this exam")
	subject = models.CharField(max_length = 20, validators = [validate_fields], null = False, blank = False)
	start = models.DateTimeField(default = timezone.now)
	teacher = models.CharField(max_length = 20)

	def __str__(self):
		return self.skillType


class Question(models.Model):
	question = models.TextField(null = False, blank = False)
	ans = models.CharField(max_length = 20, null=False, blank = False)
	op2 = models.CharField(max_length = 20, null = False, blank = False)
	op3 = models.CharField(max_length = 20, null = False, blank = False)
	op4 = models.CharField(max_length = 20, null = False, blank = False)
	exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
	
	def __str__(self):
		return self.question

	def get_fields(self):
		#fields = [(field.name, field.value_to_string(self)) for field in Question._meta.fields[2:-2]]
		fields = [field.value_to_string(self) for field in Question._meta.fields[2:-1]]
		shuffle(fields)
		return fields

	def save(self, *args, **kwargs):
		if len({self.ans, self.op2, self.op3, self.op4}) != 4:
			raise ValidationError(_("duplicate options"))
		super(Question, self).save(*args, **kwargs)


class Message(models.Model):
	title = models.CharField(max_length = 30)
	msg = models.TextField()
	student = models.ForeignKey(User, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
	 	#return reverse('msg-detail', kwargs={'pk':self.pk})
	 	return reverse('mouni:msg-detail', kwargs={'pk':self.pk}) #called on creation of new message

	def get_fields(self):
		fields = [(field.name, field.value_to_string(self)) for field in Message._meta.fields]
		shuffle(fields)
		return fields


class ResultPerExam(models.Model):
	student = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	exam = models.ForeignKey(Exam, on_delete = models.DO_NOTHING)
	marks = models.PositiveIntegerField(editable = False)
	total_marks = models.PositiveIntegerField(editable = False)
	remarks = models.TextField()
	que_pick_ans = models.TextField() #just storing queid:0 or 1 #modify it to store question_id : chosen_option_number : correct_option_number
	seed = models.PositiveIntegerField(editable = False)


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from random import shuffle
import random

class Exam(models.Model):
	skillType = models.CharField(max_length = 20)
	subject = models.CharField(max_length = 20)
	start = models.DateTimeField(default = timezone.now)
	teacher = models.CharField(max_length = 20)

	def __str__(self):
		return self.skillType


class Question(models.Model):
	question = models.TextField()
	ans = models.CharField(max_length = 20)
	op2 = models.CharField(max_length = 20)
	op3 = models.CharField(max_length = 20)
	op4 = models.CharField(max_length = 20)
	exam = models.ForeignKey(Exam, on_delete = models.CASCADE)
	skill = models.CharField(max_length = 20)
	
	def __str__(self):
		return self.question

	def get_fields(self):
		#fields = [(field.name, field.value_to_string(self)) for field in Question._meta.fields[2:-2]]
		fields = [field.value_to_string(self) for field in Question._meta.fields[2:-2]]
		shuffle(fields)
		return fields

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
	que_pick_ans = models.TextField() #just storing queid:0 or 1 #modify it to store question_id : chosen_option_number : correct_option_number
	seed = models.PositiveIntegerField(editable = False)


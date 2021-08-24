from django import forms
from django.forms import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields




class NewUserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ("username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ["title","body","status","tags"]
		widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }

class AnswerForm(forms.ModelForm):
	class Meta:
		model = Answer
		fields=["body"]
		widgets = {
			"body": forms.Textarea(attrs={"class": "form-control"}),
		}
	
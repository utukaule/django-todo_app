from django import forms
from django.forms import ModelForm

from .models import *

class My_todoForm(forms.ModelForm):
	class Meta:
		model = My_todo
		fields = '__all__'
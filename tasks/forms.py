from django import forms
from django.forms import ModelForm
from django.forms import Textarea

from .models import *

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            # 'description': Textarea(attrs={'cols': 80, 'rows': 20}),
        }
from dataclasses import fields
from pyexpat import model
from sys import implementation
from .models import Question, AppUser
from django import forms
class CreateQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('question_title', 'option_A', 'option_B', 'option_C', 'option_D', 'correct_ans')

class LoginForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ('email', 'password')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = '__all__'
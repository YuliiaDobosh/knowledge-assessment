from django import forms
from .models import Test, Answer

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'description']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['student', 'question', 'selected_answer']

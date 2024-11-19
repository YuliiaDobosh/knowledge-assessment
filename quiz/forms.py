# -*- coding: utf-8 -*-
from django import forms
from .models import Test, Result

# Форма для створення нового тесту
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['question', 'correct_answer']
        labels = {
            'question': 'Питання',
            'correct_answer': 'Правильна відповідь'
        }

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        self.fields['question'].widget.attrs['placeholder'] = 'Введіть питання тесту'
        self.fields['correct_answer'].widget.attrs['placeholder'] = 'Введіть правильну відповідь'

# Форма для оцінки результатів тесту
class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['student', 'test', 'score']
        labels = {
            'student': 'Студент',
            'test': 'Тест',
            'score': 'Оцінка'
        }

    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.fields['student'].widget.attrs['placeholder'] = 'Оберіть студента'
        self.fields['test'].widget.attrs['placeholder'] = 'Оберіть тест'
        self.fields['score'].widget.attrs['placeholder'] = 'Введіть оцінку'

# Форма для відповіді на тест
class TestAnswerForm(forms.Form):
    answer = forms.CharField(max_length=255, label="Ваша відповідь")

    def __init__(self, *args, **kwargs):
        super(TestAnswerForm, self).__init__(*args, **kwargs)
        self.fields['answer'].widget.attrs['placeholder'] = 'Введіть вашу відповідь'

# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import TestForm, TestAnswerForm  # Імпортуємо форму для відповіді
from .models import Test, Result, Student
from django.shortcuts import render
# manage.py для коректного перетворення файлів

def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_list')  # Перехід до списку тестів
    else:
        form = TestForm()
    return render(request, 'quiz/create_test.html', {'form': form})

def take_test(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.method == 'POST':
        form = TestAnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            score = 1 if answer == test.correct_answer else 0
            # Збереження результату тестування
            Result.objects.create(
                student=Student.objects.get(email=request.user.email),
                test=test,
                score=score
            )
            return redirect('test_list')  # Перехід до списку тестів після відповіді
    else:
        form = TestAnswerForm()
    return render(request, 'quiz/take_test.html', {'form': form, 'test': test})

def student_results(request):
    student = Student.objects.get(email=request.user.email)
    results = Result.objects.filter(student=student)
    total_score = Result.calculate_total_score(student)
    return render(request, 'quiz/student_results.html', {
        'results': results,
        'total_score': total_score,
    })

def home(request):
    return render(request, 'quiz/home.html')

# quiz/views.py
from django.shortcuts import render, redirect
from .forms import TestForm, TestAnswerForm
from .models import Test, Result, Student

# Головна сторінка
def home(request):
    return render(request, 'quiz/home.html')

# Створення нового тесту
def create_test(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Перехід до головної сторінки
    else:
        form = TestForm()
    return render(request, 'quiz/create_test.html', {'form': form})

# Проходження тесту
def take_test(request, test_id):
    test = Test.objects.get(id=test_id)
    if request.method == 'POST':
        # Отримуємо введене ім'я користувача
        user_name = request.POST.get('name')
        answer = request.POST.get('answer')
        score = 1 if answer == test.correct_answer else 0

        # Зберігаємо студента, якщо він ще не є в базі
        student, created = Student.objects.get_or_create(name=user_name, email=request.user.email)

        # Зберігаємо результат
        Result.objects.create(
            student=student,
            test=test,
            score=score,
        )

        return redirect('student_result')  # Перехід до результатів студента
    return render(request, 'quiz/take_test.html', {'test': test})

# Перегляд результатів студента
def student_result(request):
    # Отримуємо студента за email
    student = Student.objects.get(email=request.user.email)
    
    # Отримуємо всі результати цього студента
    results = Result.objects.filter(student=student)
    
    # Обчислюємо загальний бал
    total_score = Result.calculate_total_score(student.name)
    
    # Повертаємо шаблон з результатами
    return render(request, 'quiz/student_result.html', {
        'results': results,
        'total_score': total_score,
    })

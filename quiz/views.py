import os
import django
from multiprocessing import Pool
from django.shortcuts import render, redirect
from .models import Question, Answer
django.setup()

# Функція ініціалізації Django
def initialize_django():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'knowledge_assessment.settings')
    django.setup()

# Основні представлення
def index(request):
    return render(request, 'quiz/index.html')

def test_view(request):
    questions = Question.objects.prefetch_related("answer_set").all()
    return render(request, "quiz/test.html", {"questions": questions})

def submit_test(request):
    if request.method == "POST":
        questions = Question.objects.all()
        answers_to_check = []

        for question in questions:
            selected_answer_id = request.POST.get(f"question_{question.id}")
            if selected_answer_id:
                answers_to_check.append(int(selected_answer_id))

        # Ініціалізація Django перед запуском процесів
        initialize_django()

        # Перевірка відповідей паралельно
        with Pool() as pool:
            results = pool.map(check_answer, answers_to_check)

        correct_count = sum(results)
        total_questions = len(questions)

        # Зберігаємо результати в сесії
        request.session["correct_count"] = correct_count
        request.session["total_questions"] = total_questions

        return redirect("test_results")
    else:
        return redirect("test_view")

# Підрахунок правильної відповіді
def check_answer(selected_answer_id):
    # Ініціалізація Django в процесі
    initialize_django()
    
    try:
        selected_answer = Answer.objects.get(id=selected_answer_id)
        return selected_answer.is_correct
    except Answer.DoesNotExist:
        return False

def test_results(request):
    correct_count = request.session.get("correct_count", 0)
    total_questions = request.session.get("total_questions", 0)
    return render(request, "quiz/result.html", {
        "correct_count": correct_count,
        "total_questions": total_questions
    })
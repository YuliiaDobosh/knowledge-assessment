# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Головна сторінка
    path('create_test/', views.create_test, name='create_test'),  # Створення тесту
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),  # Проходження тесту
    path('student_result/', views.student_result, name='student_result'),  # Перегляд результатів
]

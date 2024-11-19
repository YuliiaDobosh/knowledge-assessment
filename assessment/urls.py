from django.urls import path, include  # Додано include для імпорту 
from django.contrib import admin  # Імпортуємо адмін панель
from quiz import views  # Імпортуємо views з додатку quiz

urlpatterns = [
    path('admin/', admin.site.urls),  # Реєстрація адмін панелі
    path('quiz/', include('quiz.urls')),  # Підключення URL-ів для додатку quiz
    path('', views.home, name='home'),  # Головна сторінка
]

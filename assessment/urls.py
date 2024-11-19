from django.urls import path, include
from django.contrib import admin
from quiz import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Реєстрація адмін панелі
    path('', views.home, name='home'),  # Головна сторінка
    path('quiz/', include('quiz.urls')),  # Підключення URL-ів для додатку quiz
]

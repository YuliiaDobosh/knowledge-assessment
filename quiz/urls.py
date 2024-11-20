from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # головна сторінка
    path('test/', views.test_view, name='test'),  # сторінка тесту
    path('submit_test/', views.submit_test, name='submit_test'),  # обробка відправки тесту
    path('results/', views.test_results, name='test_results'),  # сторінка результатів
]

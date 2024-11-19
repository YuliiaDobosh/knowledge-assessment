from django.urls import path
from . import views

urlpatterns = [
    path('create_test/', views.create_test, name='create_test'),
    path('take_test/<int:test_id>/', views.take_test, name='take_test'),
    path('student_results/', views.student_results, name='student_results'),
]

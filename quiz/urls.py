from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test_view, name='test_view'),
    path('submit/', views.submit_test, name='submit_test'),
    path('results/', views.test_results, name='test_results'),
]

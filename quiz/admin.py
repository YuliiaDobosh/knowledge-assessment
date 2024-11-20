from django.contrib import admin
from .models import Test, Result, Student, Question, UserAnswer, Answer

# Реєстрація всіх моделей
admin.site.register(Test)
admin.site.register(Result)
admin.site.register(Student)
admin.site.register(Question)  # Переконайтесь, що ця модель зареєстрована
admin.site.register(UserAnswer)  # Переконайтесь, що ця модель зареєстрована
admin.site.register(Answer)
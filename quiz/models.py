# quiz/models.py
from django.db import models

# Модель для зберігання інформації про студентів
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

# Модель для зберігання інформації про тест
class Test(models.Model):
    question = models.CharField(max_length=500)  # Запитання тесту
    correct_answer = models.CharField(max_length=100)  # Правильна відповідь

    def __str__(self):
        return self.question

# Модель для зберігання результатів тесту
class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Зв'язок з студентом
    test = models.ForeignKey(Test, on_delete=models.CASCADE)  # Зв'язок з тестом
    score = models.IntegerField()  # Бали за тест

    @staticmethod
    def calculate_total_score(student_name):
        # Обчислюємо загальний бал для студента
        total_score = Result.objects.filter(student__name=student_name).aggregate(models.Sum('score'))['score__sum']
        return total_score or 0

    def __str__(self):
        return f'{self.student.name} - {self.test.question} - {self.score}'

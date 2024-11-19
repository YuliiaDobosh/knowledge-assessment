# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime, timedelta
from django.contrib import admin
# manage.py для виклику перекодування файлу

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Test(models.Model):
    question = models.TextField()
    correct_answer = models.TextField()

    def __str__(self):
        return self.question

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()

    @classmethod
    def calculate_total_score(cls, student):
        return cls.objects.filter(student=student).aggregate(models.Sum('score'))['score__sum'] or 0


class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test', 'score')  # Виводимо студентів, тести та оцінки
    search_fields = ('student__name', 'test__question')  # Пошук за іменем студента та питанням тесту

    def __str__(self):
        return f"{self.student.name} - {self.test.question} - {self.score}"

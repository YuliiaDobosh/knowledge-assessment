from django.db import models

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

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'test', 'score')  # Відображення полів у списку
    search_fields = ('student__name', 'test__question')  # Додати можливість пошуку

    def __str__(self):
        return f"{self.student.name} - {self.test.question} - {self.score}"

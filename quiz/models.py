from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Result(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    score = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer_set")
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=255)

    def is_correct(self):
        return self.user_answer == self.question.correct_answer
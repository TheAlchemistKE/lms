from django.db import models


# Create your models here.
class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    administer_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)


class AnswerOptions(models.Model):
    id = models.AutoField(primary_key=True)
    option_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)




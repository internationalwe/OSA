from django.db import models

# Create your models here.


class Question(models.Model):
    question_subject = models.CharField(max_length=200)
    question_text = models.TextField()

    def __str__(self):
        return self.question_subject


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

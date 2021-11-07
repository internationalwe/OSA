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


class Post(models.Model):
    drink_count = models.IntegerField()
    drink_amount = models.IntegerField()
    smoke_yn = models.IntegerField()
    smoke_amount = models.IntegerField()
    exercise_count = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    family_stroke = models.IntegerField()
    family_highBlood = models.IntegerField()
    family_diabetes = models.IntegerField()
    family_etc = models.IntegerField()

    def __str__(self):
        return self.drink_count

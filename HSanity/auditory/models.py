from django.db import models
from establishment.models import Establishment
from django.contrib.auth.models import User

# Create your models here.

class Audit(models.Model):
    id = models.AutoField(primary_key=True)
    establishment = models.ManyToManyField(Establishment)
    created = models.DateTimeField(auto_now_add=True)
    scoreToPass = models.IntegerField(help_text="Final audit rating")
    score = models.FloatField(default=0)

    def __str__(self):
        return f"{self.id}-{self.establishment.all()}-{self.created}"

    def get_questions(self):
        return self.question_set.all


class Section(models.Model):
    name = models.CharField(max_length=50)
    numOfQuestions = models.IntegerField()
    scoreToPass = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Question(models.Model):
    text = models.CharField(max_length=255)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

    def get_answers(self):
        return self.answer_set.all


class Answer(models.Model):
    text = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question.text}, Answer: {self.text}, Correct: {self.correct}"


class AuditResult(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk}"


class SectionResult(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.pk}"

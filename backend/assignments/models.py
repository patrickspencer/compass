from django.db import models

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    max_problem_attempts = models.SmallIntegerField()
    start_datetime = models.DateTimeField()
    due_date = models.DateTimeField()
    reduced_credit_due_date = models.DateTimeField()

class Problem(models.Model):
    value = models.CharField(max_length=40000)
    seed = models.BigIntegerField()
    start_datetime = models.DateTimeField()
    grade = models.CharField(max_length=200)
    attempts = models.PositiveIntegerField()
    template_id = models.IntegerField()
    assignments = models.ManyToManyField(Assignment)

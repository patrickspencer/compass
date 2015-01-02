from django.db import models

# Create your models here.

class UserProfile(models.Model):
    assignments = models.ManyToManyField(Assignment)

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.CharField(max_length=200)
    due_date = models.CharField(max_length=200)

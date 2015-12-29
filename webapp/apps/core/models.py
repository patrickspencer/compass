from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = 'users'

class Problem(models.Model):
    value = models.TextField()

    class Meta:
        db_table = 'problems'

class ProblemMapping(models.Model):
    user_id = models.ForeignKey(User)
    problem_id = models.ForeignKey(Assignment)
    seed = models.PositiveSmallIntegerField()
    # assignment_id = models.ForeignKey(Assignment)
    # assignment_order = models.ForeignKey(Assignment)

    class Meta:
        db_table = 'problem_mappings'


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assignments'

    def __unicode__(self):
        return self.name


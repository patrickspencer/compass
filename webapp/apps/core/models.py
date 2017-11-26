from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Order of the classes is important

class Problem(models.Model):
    value = models.TextField()

    class Meta:
        db_table = 'problems'

class Assignment(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'assignments'

    def __unicode__(self):
        return self.name

class User(AbstractUser):
    problems = models.ManyToManyField(Problem, through='ProblemMapping')
    assignments = models.ManyToManyField(Assignment, through='AssignmentMapping')

    class Meta:
        db_table = 'users'


class AssignmentMapping(models.Model):
    user_id = models.ForeignKey(User)
    assignment = models.ForeignKey(Assignment)

    class Meta:
        db_table = 'assignment_mappings'

class ProblemMapping(models.Model):
    user = models.ForeignKey(User)
    problem_id = models.ForeignKey(Problem)
    seed = models.PositiveSmallIntegerField()
    assignment_mapping_id = models.ForeignKey(AssignmentMapping, null=True)
    # assignment_order = models.ForeignKey(Assignment)

    class Meta:
        db_table = 'problem_mappings'

class Answer(models.Model):
    value = models.TextField()
    user_id = models.ForeignKey(User)
    problem_mapping_id = models.ForeignKey(ProblemMapping)

    class Meta:
        db_table = 'answers'

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Assignment(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    due_date = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    assignments = models.ManyToManyField(Assignment)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)



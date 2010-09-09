from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    greeting = models.CharField(max_length=128)
    image_file = models.CharField(max_length=128)
#    user = models.ForeignKey(User, unique=True)
    user = models.OneToOneField(User)

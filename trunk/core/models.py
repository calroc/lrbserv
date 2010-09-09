from django.db import models
from django.contrib.auth.models import User, permalink


class UserProfile(models.Model):
    greeting = models.CharField(max_length=128)
    image_file = models.CharField(max_length=128)
#    user = models.ForeignKey(User, unique=True)
    user = models.OneToOneField(User)

    @permalink
    def get_absolute_url(self):
        return (
            'profiles_profile_detail',
            (),
            dict(username=self.user.username),
            )

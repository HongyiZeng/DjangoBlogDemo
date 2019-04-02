from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):  # ①
    user = models.OneToOneField(User, unique=True)  # ②
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)

from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import choices

class User(BaseUser):
    objects = BaseUserManager()
    username = None

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)

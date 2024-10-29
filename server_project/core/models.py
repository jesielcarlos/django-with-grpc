from django.db import models
from django.contrib.auth.models import User


class CustomUsers(User):
    is_activated = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=255
    )
    class Meta:
        app_label = 'core'
         
    def __str__(self):
        return self.username

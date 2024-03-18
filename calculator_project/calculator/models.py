from django.db import models
from django.contrib.auth.models import User

class UserAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} : {self.action}"

from unicodedata import name
from django.db import models
from app.models import Schedule
from django.contrib.auth.models import User

class UserSchedule(models.Model):
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    name = models.ForeignKey(Schedule , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.name}'

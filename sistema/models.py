from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=255)
    # Outros campos relevantes para o time

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username
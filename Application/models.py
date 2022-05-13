import jsonfield
from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=60, null=True)
    zone = models.CharField(max_length=60, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username}'


class Command(models.Model):
    nom = models.CharField(max_length=45, null=True)
    prenom = models.CharField(max_length=45, null=True)
    telephone = models.IntegerField(null=True)
    zone = models.CharField(max_length=50, null=True)
    ouvrier = models.CharField(max_length=50)
    target = models.TextField(null=True)

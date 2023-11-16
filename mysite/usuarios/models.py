from django.db import models

# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)


class Juegos(models.Model):
    username = models.CharField(max_length=30)
    snakeScore = models.IntegerField()
    tictacX = models.IntegerField()
    tictac0 = models.IntegerField()
    pongScore = models.IntegerField()
    hangmanScore = models.IntegerField()
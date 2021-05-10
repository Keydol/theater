from django.db import models

# Create your models here.

class Spectacle(models.Model):
    name = models.CharField(max_length=200)
    year = models.SmallIntegerField()
    budget = models.IntegerField()


class Repetition(models.Model):
    spectacle_id = models.ForeignKey(Spectacle, on_delete=models.CASCADE)
    datetime = models.DateTimeField()


class Actor(models.Model):
    name = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    experience = models.SmallIntegerField()


class SpectacleActors(models.Model):
    spectacle_id = models.ForeignKey(Spectacle, on_delete=models.CASCADE)
    actor_id = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    contract_price = models.IntegerField()
    premium = models.IntegerField()

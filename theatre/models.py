from django.db import models

class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()

    def __str__(self):
        return self.title

class TheatreHall(models.Model):
    name = models.CharField(max_length=255)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

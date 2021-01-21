from django.db import models

class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title
from django.db import models


class City(models.Model):

    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name

# Create your models here.

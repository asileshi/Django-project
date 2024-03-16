from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 100)
    age = models.IntegerField()

class Color(models.Model):
    color_name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.color_name
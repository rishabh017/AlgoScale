from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    hometown=models.CharField(max_length=200)

    def __str__(self):
        return self.name

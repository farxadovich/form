from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(null=True, max_length=50, blank=True)
    age = models.IntegerField(null=True, blank=True)
    emeil = models.EmailField()

    def __str__(self):
        return self.name

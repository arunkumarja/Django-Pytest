from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    dept=models.CharField(max_length=20)
    email=models.EmailField()
    # password=models.CharField(max_length=20)

    def __str__(self):
        return self.name




from django.db import models

class UserInput(models.Model):
    input1 = models.CharField(max_length=100)
    input2 = models.CharField(max_length=100)

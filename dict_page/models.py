from django.db import models
import json

class Dictionary(models.Model):
     word = models.CharField(max_length=50)
     definition = models.CharField(max_length=1000)

     def __str__(self):
         return self.word + ' : ' + self.definition





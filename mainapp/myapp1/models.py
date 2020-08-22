from django.db import models
from django.urls import reverse

# Create your models here.

class MyModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    money_take = models.IntegerField(default=0)
    money_give = models.IntegerField(default=0)

    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        reverse('list_view')
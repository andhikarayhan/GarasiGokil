from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    amount = models.IntegerField()
    engine_spec = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.brand} {self.model}"

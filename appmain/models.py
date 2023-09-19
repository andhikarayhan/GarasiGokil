from django.db import models


class Item(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    amount = models.IntegerField()
    engine_spec = models.TextField()

    def __str__(self):
        return f"{self.brand} {self.model}"

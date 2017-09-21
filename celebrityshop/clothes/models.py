from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Cloth(models.Model):
    celebrities = models.ManyToManyField(Celebrity, blank=True, related_name='clothes')
    item_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.PositiveSmallIntegerField()
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=255)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    image = models.ImageField(models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

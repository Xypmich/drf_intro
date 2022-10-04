from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

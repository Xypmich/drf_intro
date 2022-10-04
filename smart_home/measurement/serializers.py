from rest_framework import serializers

from .models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'created_at']


class SensorAllDataSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True, required=False)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
# TODO: опишите необходимые сериализаторы

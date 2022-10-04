# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorAllDataSerializer


class SensorsViewCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorsUpdateRetrieve(RetrieveUpdateAPIView):
    data = Sensor.objects.all() + Measurement.objects.all()
    queryset = data
    serializer_class = SensorAllDataSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

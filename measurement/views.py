from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorsView(ListAPIView, CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorsURView(UpdateAPIView, RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

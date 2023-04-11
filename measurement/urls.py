from django.urls import path
from .views import SensorsView, SensorsURView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsURView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]

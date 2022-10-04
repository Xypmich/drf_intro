from django.urls import path

from .views import SensorsViewCreate, SensorsUpdateRetrieve, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorsUpdateRetrieve.as_view()),
    path('measurements/', MeasurementCreate.as_view())
]

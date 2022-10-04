from django.urls import path

from .views import SensorsViewCreate, SensorsUpdateRetrieve, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors-data/<pk>/', SensorsUpdateRetrieve.as_view()),
    path('measurement/', MeasurementCreate.as_view())
    # TODO: зарегистрируйте необходимые маршруты
]

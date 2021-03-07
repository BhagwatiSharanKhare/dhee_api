from django.urls import path
from weather_api import views

urlpatterns = [
path('weather/', views.WeatherApiView.as_view()),
]

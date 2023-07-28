from django.urls import path
from .views import StationnView, StationRudView
urlpatterns = [
    path('station/', StationnView.as_view()),
    path('station/<pk>/', StationRudView.as_view()),
]
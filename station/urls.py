from django.urls import path
from .views import StationView, StationDetailView
urlpatterns = [
    path('station/', StationView.as_view()),
    path('station/<pk>/', StationDetailView.as_view()),
]
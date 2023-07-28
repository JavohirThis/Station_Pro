from django.urls import path
from .views import AdminView, AdminDetailView
urlpatterns = [
    path('Admin/', AdminView.as_view()),
    path('Admin/<pk>/', AdminDetailView.as_view()),
]
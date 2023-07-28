from django.urls import path
from .views import (UserListCreateView,UserRUDView,BronListCreateView,BronRUDView)


urlpatterns = [
    path('', UserListCreateView.as_view()),
    path('<pk>', UserRUDView.as_view()),
    path('bron/', BronListCreateView.as_view()),
    path('bron/<pk>', BronRUDView.as_view()),
]
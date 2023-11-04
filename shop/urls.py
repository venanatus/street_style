from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cloth/<int:pk>', views.cloth_detail, name='cloth_detail'),
]

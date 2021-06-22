from django.urls import path, include
from .views import views_cep

urlpatterns = [
    path('', views_cep),
]
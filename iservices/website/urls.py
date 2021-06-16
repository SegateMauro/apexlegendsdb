from django.urls import path, include
from .views import hello_blog
from .views import home

urlpatterns = [
    path('', home),
    path('hello_blog/', hello_blog)
]
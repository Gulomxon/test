from django.urls import path
from .views import *

# for creating my page urls
urlpatterns = [
    path('home', home, name='home'),
]
from django.urls import path
from .views import *

# for creating my page urls
urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('test/', test, name='test'),
]
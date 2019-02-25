from django.urls import path
from .views import home

urlpatterns = [
 path('contact/', home, name='contact')
]
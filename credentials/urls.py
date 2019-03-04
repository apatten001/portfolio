from django.urls import path
from .views import UnderConstruction

urlpatterns = [
    path('', UnderConstruction.as_view(), name='home')
]

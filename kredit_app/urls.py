from django.urls import path
from . import views

urlpatterns = [
    path('', views.hitung_kredit, name='hitung_kredit'),
]

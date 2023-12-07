from django.urls import path
from . import views

urlpatterns = [
    path('', views.predictor, name='predictor'),
    path('resultado', views.formInfo, name='resultado')
]
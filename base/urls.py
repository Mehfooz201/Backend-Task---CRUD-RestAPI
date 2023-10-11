
from django.urls import path
from . import views


urlpatterns = [
     path('product/', views.home, name='home')
]

from django.urls import path
from api import views

urlpatterns = [
    path('getstate/', views.getstate, name = 'getstate'),
    path('run/', views.run),
]
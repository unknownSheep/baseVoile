from django.urls import path
from . import views


urlpatterns = [
    path('', views.rent, name='rent'),
    path('materiel/', views.gear, name='gear'),
    path('adherents/', views.adherents, name='adherents'),
]

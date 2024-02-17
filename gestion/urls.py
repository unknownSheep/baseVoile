from django.urls import path
from . import views


urlpatterns = [
    path('', views.rent, name='rent'),
    path('materiel/', views.gear, name='gear'),
    path('adherents/', views.adherents, name='adherents'),
    path('reparations/', views.repair, name='reparations'),
    path('historique/', views.history, name='historique'),
]

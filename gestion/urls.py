from django.urls import path
from . import views


urlpatterns = [
    path('', views.emprunts, name='emprunts'),
    path('materiel/', views.materiel, name='materiel'),
    path('adherents/', views.adherents, name='adherents'),
    path('reparations/', views.repair, name='reparations'),
    path('historique/', views.history, name='historique'),
]

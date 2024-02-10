from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gear/', views.gear, name='gear'),
    path('adherents/', views.adherents, name='adherents'),
    path('rent/', views.rent, name='rent')
]

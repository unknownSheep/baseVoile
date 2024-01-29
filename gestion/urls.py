from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gear/', views.gear, name='login'),
    path('adherents/', views.adherents, name='login')
]

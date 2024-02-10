from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Adherent, Gear


# Option pour trier


def index(request):
    return HttpResponse("index")


def gear(request):
    context = {"gear": Gear.objects.all()}
    return render(request, "gestion/listGear.html", context)


def adherents(request):
    context = {"adherents": Adherent.objects.all()}
    return render(request, "gestion/listAdherent.html", context)


def rent(request):
    return HttpResponse("emprunt")


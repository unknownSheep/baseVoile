from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Adherent, Gear, Rentals


# Option pour trier


def rent(request):
    context = {"emprunts": Rentals.objects.all()}
    return render(request, "gestion/index.html", context)


def gear(request):  # TODO: add sorting by name/cat...
    context = {"materiel": Gear.objects.all()}
    return render(request, "gestion/materiel.html", context)


def adherents(request):  # TODO: add sorting by name...
    context = {"adherents": Adherent.objects.all()}
    return render(request, "gestion/adherents.html", context)


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone
from .models import Adherent, Gear, Rentals


def rent(request):
    print()
    context = {
        "sortis":  Rentals.objects.filter(returnTime__isnull=True).order_by('startTime'),
        "rentres": Rentals.objects.filter(returnTime__isnull=False).filter(startTime__day=timezone.now().day).order_by('startTime')
    }
    return render(request, "gestion/index.html", context)


def gear(request):  # TODO: add sorting by name/cat...
    context = {"materiel": Gear.objects.all()}
    return render(request, "gestion/materiel.html", context)


def adherents(request):  # TODO: add sorting by name...
    context = {"adherents": Adherent.objects.all()}
    return render(request, "gestion/adherents.html", context)


from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .forms import RentForm
from .models import Adherent, Gear, Rentals


def rent(request): # TODO: retour + degats et mise en page du form de l'ajout

    if request.method == 'POST':
        form = RentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('rent')
    else:
        form = RentForm()

    context = {
        "form": form,
        "sortis":  Rentals.objects.filter(returnTime__isnull=True).filter(startTime__day=timezone.now().day)
                                                                  .filter(startTime__month=timezone.now().month)
                                                                  .filter(startTime__year=timezone.now().year)
                                                                  .order_by('startTime'),
        "rentres": Rentals.objects.filter(returnTime__isnull=False).filter(returnTime__day=timezone.now().day)
                                                                   .filter(returnTime__month=timezone.now().month)
                                                                   .filter(returnTime__year=timezone.now().year)
                                                                   .order_by('returnTime'),
    }
    return render(request, "gestion/index.html", context)

def gear(request):  # TODO: add sorting by name/cat...
    context = {"materiel": Gear.objects.all()}
    return render(request, "gestion/materiel.html", context)


def adherents(request):  # TODO: add sorting by name...
    context = {"adherents": Adherent.objects.all()}
    return render(request, "gestion/adherents.html", context)


def repair(request): # TODO: add sorting by name... + form de reparés
    context = {"reparer": Gear.objects.filter(toRepair=True)}
    return render(request, "gestion/reparations.html", context)


def history(request): # TODO: add sorting and filtering
    context = {"emprunts": Rentals.objects.filter(returnTime__isnull=False).filter(startTime__year=timezone.now().year).order_by('returnTime')}
    return render(request, "gestion/historique.html", context)

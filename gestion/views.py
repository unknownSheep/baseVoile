from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .forms import NouvelEmpruntForm, AdherentForm, GearForm, AddImageForm, ReparationForm
from .models import Adherent, Gear, Emprunt, Reparation


def emprunts(request):
    nouvelEmpruntForm = None
    if request.method == 'POST':
        if request.POST['action'] == 'Nouvel Emprunt':
            nouvelEmpruntForm = NouvelEmpruntForm(request.POST)
            if nouvelEmpruntForm.is_valid():
                nouvelEmpruntForm.save()
                return redirect('emprunts')

        elif request.POST['action'] == 'Retour':
            emprunt_id = int(request.POST['id'])  # NOT SAFE: should use constructor and add a hidden field
            emprunt = Emprunt.objects.get(id=emprunt_id)
            emprunt.returnTime = timezone.now()
            emprunt.save()
            return redirect('emprunts')
    else:
        nouvelEmpruntForm = NouvelEmpruntForm()

    context = {
        "pageName": "emprunts",
        "nouvelEmpruntForm": nouvelEmpruntForm,
        "sortis": Emprunt.objects.filter(returnTime__isnull=True).order_by('startTime'),
        "rentres": Emprunt.objects.filter(returnTime__isnull=False).filter(startTime__day=timezone.now().day)
        .filter(startTime__month=timezone.now().month)
        .filter(startTime__year=timezone.now().year)
        .order_by('-returnTime'),
    }
    return render(request, "gestion/emprunts.html", context)


def materiel(request, option):
    newGearForm = None
    addImageForm = None

    if request.method == 'POST':
        if request.POST['action'] == 'Ajouter':
            newGearForm = GearForm(request.POST, request.FILES)
            if newGearForm.is_valid():
                newGearForm.save()
                return redirect('materiel', 0)

        elif request.POST['action'] == 'Envoyer':
            addImageForm = AddImageForm(request.POST, request.FILES)
            gear_id = int(request.POST['id'])
            if addImageForm.is_valid():
                g = Gear.objects.get(id=gear_id)
                imageFile = request.FILES['photo']
                g.photo = imageFile
                g.save()
                return redirect('materiel', 0)

        elif request.POST['action'] == 'Retirer':
            gear_id = int(request.POST['id'])
            g = Gear.objects.get(id=gear_id)
            g.isInService = not g.isInService
            g.save()
            return redirect('materiel', option)

        elif request.POST['action'] == 'Supprimer photo':
            gear_id = int(request.POST['id'])
            g = Gear.objects.get(id=gear_id)
            g.photo = None
            g.save()
            return redirect('materiel', option)

    else:
        newGearForm = GearForm()
        addImageForm = AddImageForm()

    l = None
    if option == 1:
        l = Gear.objects.filter(isInService=False).order_by('category')
    else:
        l = Gear.objects.filter(isInService=True).order_by('category')

    context = {
        "newGearForm": newGearForm,
        "addImageForm": addImageForm,
        "materiel": l,
        "pageName": "materiel",
        "option": option,
    }
    return render(request, "gestion/materiel.html", context)


def adherents(request):
    nouvelAdherentForm = None
    if request.method == 'POST':
        nouvelAdherentForm = AdherentForm(request.POST, request.FILES)
        if nouvelAdherentForm.is_valid():
            nouvelAdherentForm.save()
            return redirect('adherents')
    else:
        nouvelAdherentForm = AdherentForm()

    context = {"adherents": Adherent.objects.all(),
               "pageName": "adherents",
               "addForm": nouvelAdherentForm
               }
    return render(request, "gestion/adherents.html", context)


def repair(request):
    repa_form = None
    if request.method == "POST":
        if request.POST["action"] == "Reparé":
            repa_id = int(request.POST['id'])
            repa = Reparation.objects.get(id=repa_id)
            repa.dateFin = timezone.now()
            repa.save()
            return redirect('reparations')
        elif request.POST["action"] == "Ajouter":
            repa_form = ReparationForm(request.POST)
            if repa_form.is_valid():
                repa_form.save()
                return redirect('reparations')
    else:
        repa_form = ReparationForm()

    context = {
        "pageName": "repair",
        "reparations": Reparation.objects.filter(dateFin__isnull=True),
        "repaForm": repa_form,
    }
    return render(request, "gestion/reparations.html", context)


def history(request):
    context = {"emprunts": Emprunt.objects.filter(returnTime__isnull=False).filter(
        startTime__year=timezone.now().year).order_by('-returnTime'),
               "pageName": "historique",
               }
    return render(request, "gestion/historique.html", context)


def surveillance(request):
    context = {
        "pageName": "surveillance",
        "sortis": Emprunt.objects.filter(returnTime__isnull=True)
        .filter(startTime__day=timezone.now().day)
        .filter(startTime__month=timezone.now().month)
        .filter(startTime__year=timezone.now().year)
        .order_by('startTime'),
    }
    return render(request, "gestion/surveillance.html", context)





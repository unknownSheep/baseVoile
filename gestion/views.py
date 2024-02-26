from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .forms import NouvelEmpruntForm, RetourForm, AdherentForm, GearForm, AddImageForm
from .models import Adherent, Gear, Emprunt


def emprunts(request): # TODO: retour + degats et mise en page du form de l'ajout
    nouvelEmpruntForm = None
    retourForm = None
    if request.method == 'POST':
        if request.POST['action'] == 'Nouvel Emprunt':
            nouvelEmpruntForm = NouvelEmpruntForm(request.POST)
            if nouvelEmpruntForm.is_valid():
                nouvelEmpruntForm.save()
                return redirect('emprunts')

        elif request.POST['action'] == 'Retour':
            retourForm = RetourForm(request.POST)
            emprunt_id = int(request.POST['id'])  # NOT SAFE: should use constructor and add a hidden field
            if retourForm.is_valid():
                emprunt = Emprunt.objects.get(id=emprunt_id)
                emprunt.gear1IsDamaged = retourForm.cleaned_data['gear1IsDamaged']
                emprunt.gear2IsDamaged = retourForm.cleaned_data['gear2IsDamaged']
                emprunt.returnTime = timezone.now()
                emprunt.save()

                gear1 = Gear.objects.get(id=emprunt.gear1.id)
                gear1.toRepair = gear1.toRepair or retourForm.cleaned_data['gear1IsDamaged']
                gear1.save()

                if emprunt.gear2 is not None:
                    gear2 = Gear.objects.get(id=emprunt.gear2.id)
                    gear2.toRepair = gear2.toRepair or retourForm.cleaned_data['gear2IsDamaged']
                    gear2.save()

                return redirect('emprunts')
    else:
        nouvelEmpruntForm = NouvelEmpruntForm()
        retourForm = RetourForm()

    context = {
        "pageName": "emprunts",
        "nouvelEmpruntForm": nouvelEmpruntForm,
        "retourForm": retourForm,
        "sortis":  Emprunt.objects.filter(returnTime__isnull=True).order_by('startTime'),
        "rentres": Emprunt.objects.filter(returnTime__isnull=False).filter(startTime__day=timezone.now().day)
                                                                   .filter(startTime__month=timezone.now().month)
                                                                   .filter(startTime__year=timezone.now().year)
                                                                   .order_by('returnTime'),
    }
    return render(request, "gestion/emprunts.html", context)


def materiel(request):
    newGearForm = None
    addImageForm = None

    if request.method == 'POST':
        if request.POST['action'] == 'Ajouter':
            newGearForm = GearForm(request.POST, request.FILES)
            if newGearForm.is_valid():
                newGearForm.save()
                return redirect('materiel')

        elif request.POST['action'] == 'Envoyer':
            addImageForm = AddImageForm(request.POST, request.FILES)
            gear_id = int(request.POST['id'])
            if addImageForm.is_valid():
                g = Gear.objects.get(id=gear_id)
                imageFile = request.FILES['photo']
                g.photo = imageFile
                g.save()
                return redirect('materiel')

    else:
        newGearForm = GearForm()
        addImageForm = AddImageForm()

    context = {
        "newGearForm": newGearForm,
        "addImageForm": addImageForm,
        "materiel": Gear.objects.all(),
        "pageName": "materiel",
       }
    return render(request, "gestion/materiel.html", context)


def adherents(request):  # TODO:  sorting
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


def repair(request):  # TODO: sorting

    if request.method == "POST":
        if request.POST['action'] == 'Repare':
            gearId = int(request.POST['id'])
            g = Gear.objects.get(id=gearId)
            g.toRepair = False
            g.save()

    context = {"reparer": Gear.objects.filter(toRepair=True),
               "pageName": "repair",
               }
    return render(request, "gestion/reparations.html", context)


def history(request): # TODO: sorting and filtering
    context = {"emprunts": Emprunt.objects.filter(returnTime__isnull=False).filter(startTime__year=timezone.now().year).order_by('returnTime'),
               "pageName": "historique",
               }
    return render(request, "gestion/historique.html", context)

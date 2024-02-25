from django import forms

from gestion.models import Adherent, Gear, Emprunt


class NouvelEmpruntForm(forms.ModelForm):
    adherent1 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Barreur", required=True)
    adherent2 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Equipier", required=False)

    gear1 = forms.ModelChoiceField(queryset=Gear.objects.all(), label="Materiel 1", required=True)
    gear2 = forms.ModelChoiceField(queryset=Gear.objects.all(), label="Materiel 2", required=False)

    class Meta:
        model = Emprunt
        fields = ['adherent1', 'adherent2', 'gear1', 'gear2']


class AdherentForm(forms.ModelForm):
    firstname = forms.CharField(max_length=64, label="Prenom", required=True)
    surname = forms.CharField(max_length=64, label="Nom", required=True)
    email = forms.EmailField(max_length=64, label="e-mail", required=False)
    phone = forms.IntegerField(label="Tel", required=False)
    adhesion = forms.CharField(max_length=64, label="Adhesion", required=True)

    class Meta:
        model = Adherent
        fields = ['firstname', 'surname', 'email', 'phone', 'adhesion']


class RetourForm(forms.Form):
    gear1IsDamaged = forms.BooleanField(required=False, label="Materiel 1")
    gear2IsDamaged = forms.BooleanField(required=False, label="Materiel 2")

    class Meta:
        fields = ['gear1IsDamaged', 'gear2IsDamaged']



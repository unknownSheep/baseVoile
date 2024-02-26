from django import forms

from gestion.models import Adherent, Gear, Emprunt, GearCat


class NouvelEmpruntForm(forms.ModelForm):
    adherent1 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Barreur", required=True)
    adherent2 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Equipier", required=False)

    gear1 = forms.ModelChoiceField(queryset=Gear.objects.all(), label="Materiel 1", required=True)
    gear2 = forms.ModelChoiceField(queryset=Gear.objects.all(), label="Materiel 2", required=False)

    class Meta:
        model = Emprunt
        fields = ['adherent1', 'adherent2', 'gear1', 'gear2']


class AdherentForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label="NOM Prenom", required=True)
    adhesion = forms.CharField(max_length=64, label="Adhesion", required=True)

    class Meta:
        model = Adherent
        fields = ['name', 'adhesion']


class GearForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label="Nom", required=True)
    category = forms.ModelChoiceField(queryset=GearCat.objects.all(), label="Categorie", required=True)
    # photo = forms.ImageField(label="Photo", required=False)

    class Meta:
        model = Gear
        fields = ['name', 'category', 'photo']


class RetourForm(forms.Form):
    gear1IsDamaged = forms.BooleanField(required=False, label="Materiel 1")
    gear2IsDamaged = forms.BooleanField(required=False, label="Materiel 2")

    class Meta:
        fields = ['gear1IsDamaged', 'gear2IsDamaged']



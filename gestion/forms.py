from django import forms

from gestion.models import Adherent, Gear, Emprunt, GearCat, Reparation


class NouvelEmpruntForm(forms.ModelForm):
    adherent1 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Adherent 1", required=True, widget=forms.Select(attrs={'class': 'chosen-select'}))
    adherent2 = forms.ModelChoiceField(queryset=Adherent.objects.all(), label="Adherent 2", required=False, widget=forms.Select(attrs={'class': 'chosen-select'}))

    gear1 = forms.ModelChoiceField(queryset=Gear.objects.filter(isInService=True), label="Materiel 1", required=True, widget=forms.Select(attrs={'class': 'chosen-select'}))
    gear2 = forms.ModelChoiceField(queryset=Gear.objects.filter(isInService=True), label="Materiel 2", required=False, widget=forms.Select(attrs={'class': 'chosen-select'}))

    class Meta:
        model = Emprunt
        fields = ['adherent1', 'adherent2', 'gear1', 'gear2']


class AdherentForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label="NOM", required=True)
    firstName = forms.CharField(max_length=64, label="Prénom", required=True)

    class Meta:
        model = Adherent
        fields = ['name', 'firstName']


class GearForm(forms.ModelForm):
    name = forms.CharField(max_length=64, label="Nom", required=True)
    category = forms.ModelChoiceField(queryset=GearCat.objects.all(), label="Categorie", required=True)
    photo = forms.ImageField(label="Photo", required=False)

    class Meta:
        model = Gear
        fields = ['name', 'category', 'photo']


class ReparationForm(forms.ModelForm):
    gear = forms.ModelChoiceField(queryset=Gear.objects.filter(isInService=True), label="Matériel", required=True, widget=forms.Select(attrs={'class': 'chosen-select'}))
    commentaire = forms.CharField(widget=forms.Textarea, required=True, label="Commentaire")

    class Meta:
        model = Reparation
        fields = ['gear', 'commentaire']


class AddImageForm(forms.Form):
    photo = forms.ImageField(label="Ajouter image", required=True)

    class Meta:
        fields = ['photo']



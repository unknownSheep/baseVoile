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


class RetourForm(forms.Form):
    gear1IsDamaged = forms.BooleanField(required=False, label="Materiel 1")
    gear2IsDamaged = forms.BooleanField(required=False, label="Materiel 2")

    class Meta:
        fields = ['gear1IsDamaged', 'gear2IsDamaged']



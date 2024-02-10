from django import forms
from .models import Adherent, Gear, GearCat


class FormAdherent(forms.ModelForm):
    class Meta:
        model = Adherent
        fields = ['firstname', 'surname', 'email', 'phone', 'validity']
        labels = {'firstname': 'Prenom', 'surname': 'Nom', 'email': 'email', 'phone': 'Tel', 'validity': 'Validite'}


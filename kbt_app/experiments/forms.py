from django import forms
from .models import ExperimentResultat

#not used rn.

class RegistreraResultat(forms.Form):
    class Meta:
        model = ExperimentResultat
        fields = ('resultat', 'insikter', 'tro_post')
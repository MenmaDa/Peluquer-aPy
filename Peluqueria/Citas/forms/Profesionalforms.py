from django import forms
from ..models import Profesional


class ProfesionalForm(forms.ModelForm):
    class Meta:
        model = Profesional
        fields = ['nombre', 'servicios']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'servicios': forms.CheckboxSelectMultiple(),
        }
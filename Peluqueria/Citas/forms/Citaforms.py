from django import forms
from django.utils import timezone
from ..models import Cita


class CitaForm(forms.ModelForm):

    fecha_cita = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={'type': 'datetime-local'},
            format='%Y-%m-%dT%H:%M'
        ),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    class Meta:
        model = Cita
        fields = ['servicio', 'profesional', 'fecha_cita', 'prioridad']
        widgets = {
            'prioridad': forms.Select(attrs={'class': 'form-select'}),
            'servicio': forms.Select(attrs={'class': 'form-select'}),
            'profesional': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        servicio = cleaned_data.get("servicio")
        profesional = cleaned_data.get("profesional")
        fecha_cita = cleaned_data.get("fecha_cita")

        # 🔹 Validar que el profesional haga ese servicio
        if servicio and profesional:
            if not profesional.servicios.filter(id=servicio.id).exists():
                raise forms.ValidationError(
                    "El profesional seleccionado no realiza este servicio."
                )

        # 🔹 Validar que la fecha no sea en el pasado
        if fecha_cita and fecha_cita < timezone.now():
            raise forms.ValidationError(
                "No puedes agendar una cita en el pasado."
            )

        # 🔹 Validar que no esté ocupado
        if profesional and fecha_cita:
            if Cita.objects.filter(
                profesional=profesional,
                fecha_cita=fecha_cita
            ).exists():
                raise forms.ValidationError(
                    "El profesional ya tiene una cita en ese horario."
                )

        return cleaned_data
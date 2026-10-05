from django import forms
from .models import Carrera


class CarreraForm(forms.ModelForm):

    class Meta:
        model = Carrera
        fields = [
            'nombre',
            'codigo',
            'facultad',
            'duracion',
            'modalidad',
            'jornada',
            'arancel',
            'cupos',
            'correo',
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Ingeniería Informática'
            }),
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: INF-001'
            }),
            'facultad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Facultad de Ingeniería'
            }),
            'duracion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'modalidad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'jornada': forms.Select(attrs={
                'class': 'form-select'
            }),
            'arancel': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
            'cupos': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@universidad.cl'
            }),
        }

    def clean_arancel(self):
        arancel = self.cleaned_data['arancel']

        if arancel <= 0:
            raise forms.ValidationError(
                'El arancel debe ser mayor que 0.'
            )

        return arancel

    def clean_duracion(self):
        duracion = self.cleaned_data['duracion']

        if duracion <= 0:
            raise forms.ValidationError(
                'La duración debe ser mayor que 0.'
            )

        return duracion

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre'].strip()

        if not nombre:
            raise forms.ValidationError(
                'El nombre de la carrera es obligatorio.'
            )

        return nombre

    def clean_facultad(self):
        facultad = self.cleaned_data['facultad'].strip()

        if not facultad:
            raise forms.ValidationError(
                'La facultad es obligatoria.'
            )

        return facultad

    def clean_codigo(self):
        codigo = self.cleaned_data['codigo'].strip().upper()

        if not codigo:
            raise forms.ValidationError(
                'El código de la carrera es obligatorio.'
            )

        return codigo
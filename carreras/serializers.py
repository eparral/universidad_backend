from rest_framework import serializers

from .models import Carrera


class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = [
            'id',
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
        read_only_fields = ['id']

    def validate_codigo(self, value):
        return value.strip().upper()

    def validate_arancel(self, value):
        if value <= 0:
            raise serializers.ValidationError('El arancel debe ser mayor que 0.')
        if value > 100000000:
            raise serializers.ValidationError(
                'El arancel no puede superar los $100.000.000.'
            )
        return value

    def validate_cupos(self, value):
        if value > 1000:
            raise serializers.ValidationError(
                'Los cupos no pueden superar los 1.000.'
            )
        return value

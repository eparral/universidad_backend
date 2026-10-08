from rest_framework import viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

from .models import Carrera
from .serializers import CarreraSerializer


class LoginTokenView(ObtainAuthToken):
    """Valida usuario y contrasena y devuelve un token reutilizable."""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({
            'token': response.data['token'],
            'usuario': request.data.get('username'),
        })


class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all().order_by('nombre')
    serializer_class = CarreraSerializer

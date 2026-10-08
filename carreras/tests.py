from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Carrera


class CarreraAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='api-user',
            password='clave-segura-123',
        )
        self.carrera = Carrera.objects.create(
            nombre='Ingenieria Informatica',
            codigo='INF-001',
            facultad='Ingenieria',
            duracion=4,
            modalidad='Online',
            jornada='Diurna',
            arancel=2500000,
            cupos=50,
            correo='informatica@universidad.cl',
        )

    def test_login_entrega_token(self):
        response = self.client.post(reverse('api-login'), {
            'username': 'api-user',
            'password': 'clave-segura-123',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['usuario'], 'api-user')

    def test_api_rechaza_usuario_sin_token(self):
        response = self.client.get(reverse('api-carrera-list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_lista_carreras_con_token(self):
        login = self.client.post(reverse('api-login'), {
            'username': 'api-user',
            'password': 'clave-segura-123',
        })
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {login.data['token']}")

        response = self.client.get(reverse('api-carrera-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['codigo'], self.carrera.codigo)

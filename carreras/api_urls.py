from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .api_views import CarreraViewSet, LoginTokenView


router = DefaultRouter()
router.register('carreras', CarreraViewSet, basename='api-carrera')

urlpatterns = [
    path('login/', LoginTokenView.as_view(), name='api-login'),
    path('', include(router.urls)),
]

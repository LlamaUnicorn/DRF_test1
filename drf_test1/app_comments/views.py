from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Country, Manufacturer, Car, Comment
from .serializers import (
    CountrySerializer,
    ManufacturerSerializer,
    CarSerializer,
    CommentSerializer,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import exceptions
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class TokenHasScope(BasePermission):
    def has_permission(self, request, view):
        token = request.auth
        if not token:
            raise exceptions.AuthenticationFailed('Authentication credentials were not provided.')
        elif not hasattr(token, 'is_staff'):
            return False
        return token.is_staff


# class CountryViewSet(viewsets.ModelViewSet):
#     queryset = Country.objects.all()
#     serializer_class = CountrySerializer
#     permission_classes = [IsAuthenticated]


# class ManufacturerViewSet(viewsets.ModelViewSet):
#     queryset = Manufacturer.objects.all()
#     serializer_class = ManufacturerSerializer
#     permission_classes = [IsAuthenticated]


# class CarViewSet(viewsets.ModelViewSet):
#     queryset = Car.objects.all()
#     serializer_class = CarSerializer
#     permission_classes = [IsAuthenticated]  # [IsAuthenticatedOrReadOnly, TokenHasScope]


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

from .permissions import IsTokenAuthenticatedOrReadOnly


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsTokenAuthenticatedOrReadOnly]


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [IsTokenAuthenticatedOrReadOnly]


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsTokenAuthenticatedOrReadOnly]


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsTokenAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]

        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
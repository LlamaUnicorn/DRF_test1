import csv
import openpyxl

from django.http import HttpResponse
from django.views import View

from rest_framework import exceptions
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes, action


from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsTokenAuthenticatedOrReadOnly
from .models import Country, Manufacturer, Car, Comment
from .serializers import (
    CountrySerializer,
    ManufacturerSerializer,
    CarSerializer,
    CommentSerializer,
)



class TokenHasScope(BasePermission):
    def has_permission(self, request, view):
        token = request.auth
        if not token:
            raise exceptions.AuthenticationFailed('Authentication credentials were not provided.')
        elif not hasattr(token, 'is_staff'):
            return False
        return token.is_staff


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


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        permission_classes = [IsAuthenticatedOrReadOnly]

        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    

class CarExportView(View):
    def get(self, request):
        # Get the format from the query parameters
        export_format = request.GET.get('format', 'csv')

        # Get the data to be exported
        cars = Car.objects.all()

        if export_format == 'csv':
            # Export as CSV
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="cars.csv"'

            writer = csv.writer(response)
            writer.writerow(['Name', 'Manufacturer', 'Start Year', 'End Year', 'Comment Count'])

            for car in cars:
                writer.writerow([car.name, car.manufacturer.name, car.start_year, car.end_year, car.comment_set.count()])

        elif export_format == 'xlsx':
            # Export as XLSX
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="cars.xlsx"'

            workbook = openpyxl.Workbook()
            worksheet = workbook.active
            worksheet.title = 'Cars'

            worksheet['A1'] = 'Name'
            worksheet['B1'] = 'Manufacturer'
            worksheet['C1'] = 'Start Year'
            worksheet['D1'] = 'End Year'
            worksheet['E1'] = 'Comment Count'

            for car in cars:
                row = [
                    car.name,
                    car.manufacturer.name,
                    car.start_year,
                    car.end_year,
                    car.comment_set.count(),
                ]
                worksheet.append(row)

            workbook.save(response)

        else:
            # Invalid format
            response = HttpResponse('Invalid export format.', content_type='text/plain', status=400)

        return response
    


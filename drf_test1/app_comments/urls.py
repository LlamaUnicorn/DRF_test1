from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Countries
    path('countries/', views.CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('countries/<int:pk>/', views.CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='country-detail'),
    path('countries/export/', views.CountryExportView.as_view(), name='country-export'),

    # Manufacturers
    path('manufacturers/', views.ManufacturerViewSet.as_view({'get': 'list', 'post': 'create'}), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', views.ManufacturerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='manufacturer-detail'),
    path('manufacturers/export/', views.ManufacturerExportView.as_view(), name='manufacturer-export'),

    # Cars
    path('cars/', views.CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('cars/<int:pk>/', views.CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car-detail'),
    path('cars/export/', views.CarExportView.as_view(), name='car-export'),

    # Comments
    path('comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
    path('comments/export/', views.CommentsExportView.as_view(), name='comment-export'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

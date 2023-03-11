# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views

# urlpatterns = [
#     # Countries
#     path('countries/', views.CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
#     path('countries/<int:pk>/', views.CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='country-detail'),

#     # Manufacturers
#     path('manufacturers/', views.ManufacturerViewSet.as_view({'get': 'list', 'post': 'create'}), name='manufacturer-list'),
#     path('manufacturers/<int:pk>/', views.ManufacturerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='manufacturer-detail'),

#     # Cars
#     path('cars/', views.CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
#     path('cars/<int:pk>/', views.CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car-detail'),

#     # Comments
#     path('comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
#     path('comments/<int:pk>/', views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Countries
    path('countries/', views.CountryViewSet.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('countries/<int:pk>/', views.CountryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='country-detail'),

    # Manufacturers
    path('manufacturers/', views.ManufacturerViewSet.as_view({'get': 'list', 'post': 'create'}), name='manufacturer-list'),
    path('manufacturers/<int:pk>/', views.ManufacturerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='manufacturer-detail'),

    # Cars
    path('cars/', views.CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car-list'),
    path('cars/<int:pk>/', views.CarViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='car-detail'),

    # Comments
    path('comments/', views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),
    path('comments/<int:pk>/', views.CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='comment-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

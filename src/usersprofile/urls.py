from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.UsersProfileView.as_view({'get': 'retrieve'})),
    path('<int:pk>/settings/', views.UserSettingsView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('<int:pk>/bio/', views.BioSettingsView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
]
from django.urls import path, re_path
from . import views


urlpatterns = [
    re_path('(?P<pk>[0-9]+)/$', views.UsersProfileView.as_view({'get': 'retrieve'}), name='my_account'),
    path('<int:pk>/settings/', views.UserSettingsView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
    path('<int:pk>/bio/', views.BioSettingsView.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
]
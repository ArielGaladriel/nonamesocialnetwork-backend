from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/', views.UsersProfileView.as_view({'get': 'retrieve'})),
]
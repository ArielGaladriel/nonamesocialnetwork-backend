from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsListView.as_view()),
    path('create/', views.PostView.as_view({'post': 'create'})),
    path('<int:pk3>/', views.PostView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    ]


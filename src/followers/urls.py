from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk2>/', views.AddFollowerView.as_view()),
    path('', views.FollowersListView.as_view())
]
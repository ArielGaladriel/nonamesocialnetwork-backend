from django.urls import path
from . import views


urlpatterns = [
    path('followers/<int:pk2>/', views.AddDeleteFollowerView.as_view()),
    path('followers/', views.FollowersListView.as_view()),
    path('followee/', views.FolloweeListView.as_view()),
    path('followee/<int:pk2>/', views.DeleteFolloweeView.as_view())
]
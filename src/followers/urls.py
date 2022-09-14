from django.urls import path
from . import views


urlpatterns = [
    path('followers/<int:pk2>/', views.AddDeleteFollowerView.as_view()),
    path('followers/', views.FollowersListView.as_view()),
    path('followers/requested/', views.FollowersRequestsListView.as_view()),
    path('followee/', views.FolloweeListView.as_view()),
    path('followee/requested/', views.FolloweeRequestsListView.as_view()),
    path('followee/<int:pk2>/', views.UpdateDeleteFolloweeView.as_view())
]
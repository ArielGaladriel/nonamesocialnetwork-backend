from django.contrib import admin
from django.urls import path, include
from src.usersprofile import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path('usersprofile/', include('src.usersprofile.urls')),

    path('registration/', views.CreateUserView.as_view()),

]

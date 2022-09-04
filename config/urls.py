from django.contrib import admin
from django.urls import path, include
from src.usersprofile.views import MyLoginView, CreateUserView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/login/', MyLoginView.as_view(template_name='rest_framework/login.html'), name='login'),

    path('api-auth/', include('rest_framework.urls')),

    path('usersprofile/', include('src.usersprofile.urls')),

    path('registration/', CreateUserView.as_view()),

]

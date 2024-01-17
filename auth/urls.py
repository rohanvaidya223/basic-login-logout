
from django.urls import path
from django.contrib.auth import views
from .views import register,welcome

urlpatterns = [
    
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',register,name='register'),
    path('',welcome)
]

from django.urls import path
from django.contrib.auth import views
from .views import ExtendedUserLogOut,UserCreateView
from userextend.forms import AuthenticationNewForm

urlpatterns = [
        path('create_user/', UserCreateView.as_view(), name='create-user'),
        path('logout/',ExtendedUserLogOut.as_view,name='logout'),
        path("login/", views.LoginView.as_view(form_class=AuthenticationNewForm), name="login"),
]
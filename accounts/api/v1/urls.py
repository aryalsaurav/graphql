from django.urls import path

from .views import (
    UserCreateView,
    LoginView,
)
app_name = 'accounts_v1'

urlpatterns = [
    path("signup/",UserCreateView.as_view(),name="signup"),
    path('login/',LoginView.as_view(),name="login"),
]
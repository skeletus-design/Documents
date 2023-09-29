from django.urls import path

from . import views

urlpatterns = [
    path("sign_in", views.login_, name="login"),
    path("sign_up", views.register, name="register"),
    path("", views.index, name="Trella"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sign_up", views.register, name="register"),
]
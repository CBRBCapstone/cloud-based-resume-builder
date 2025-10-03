from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<int:pk>/edit/", views.edit_profile, name="edit_profile"),
    path("profile/<int:pk>/preview/", views.preview, name="preview"),
]

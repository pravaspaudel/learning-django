from django.urls import path
from .views import RegisterView,NoteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
) 

urlpatterns = [
    path("register/",RegisterView.as_view(),name="register"),

    path("login/",TokenObtainPairView.as_view(),name="login obtain"),
    path("refresh/",TokenRefreshView.as_view(),name="login refresh"),

    path("notes/",NoteView.as_view(),name="note views"),
]
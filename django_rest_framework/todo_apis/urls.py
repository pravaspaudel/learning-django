from django.urls import path
from .views import todoViews 

urlpatterns = [
    path("todos/",todoViews.as_view()),
]
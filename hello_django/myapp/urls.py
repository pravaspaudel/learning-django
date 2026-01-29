from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.home_view),
    path("users/<int:id>",views.users_view),
    path("products/<int:pid>/reviews/<int:rid>",views.product_view),
    path("homepage/",views.home_page,name="homepage"),
    path("profile/<str:username>/",views.profile_page),

    #templates
    path("temp_home/",views.home_templates),
    path("temp_about/",views.about_templates),
    path("temp_base/",views.base_templates)
]

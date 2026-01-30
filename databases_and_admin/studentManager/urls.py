from django.urls import path
from .views import add_student,update_student,delete_student,show_student

urlpatterns = [
    path("students/",show_student,name="show student"),
    path("students/add/",add_student,name="add student"),
    path("students/edit/<int:id>/",update_student,name="update student"),
    path("students/delete/<int:id>/",delete_student,name="delete student")
]
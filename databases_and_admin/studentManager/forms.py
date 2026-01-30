from django.forms import ModelForm
from .models import student_db

class StudentForm(ModelForm):
    class Meta:
        model = student_db
        fields = "__all__"
    


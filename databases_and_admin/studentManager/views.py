from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import StudentForm
from .models import student_db


#create
def add_student(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            # student_db.objects.create(
            #     name=form.cleaned_data["name"],
            #     age=form.cleaned_data["age"],
            #     grade=form.cleaned_data["grade"]
            # )
            form.save()
            return redirect("list.html")
    else:
        form = StudentForm()

    return render(request,"form.html",{"form":form})


#read
def show_student(request):
    students = student_db.objects.all()
    return render(request,"list.html",{"students":students})

#update
def update_student(request,id):

    student = get_object_or_404(student_db,id=id)
    if request.method == "POST":
        form = StudentForm(request.POST,instance=student)

        if form.is_valid():
            form.save()
            redirect("list.html")
    else:
        form = StudentForm(instance=student)
    return render(request,"form.html",{"form":form})


#delete

def delete_student(request,id):
    student = get_object_or_404(student_db,id=id)
    student.delete()
    return redirect("list.html")







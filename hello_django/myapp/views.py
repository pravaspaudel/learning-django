from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# static route
def home_view(request):
    return HttpResponse("hello this is static route")

#dynamic routes
def users_view(request,id):
    return HttpResponse(f"hello this user id is {id}")

def product_view(request,pid,rid):
    return HttpResponse(f"review for product id {pid} and review id {rid}")

#rendering html pages
def home_page(request):
    context_data = {
        "name":"harry",
        "age":32
    }
    return render(request,"index.html",context_data)

def profile_page(request,username):
    context_data = {
        "username":username
    }
    return render(request,"profile.html",context_data)


#templates and templates inheritance

def home_templates(request):
    return render(request,"home.html")
    # return HttpResponse("hello")

def about_templates(request):
    return render(request,"about.html",{"name":"hehehe","email":"hehe1234@gmail.com"})

def base_templates(request):
    return render(request,"base.html")
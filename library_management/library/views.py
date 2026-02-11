from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import Book,Borrow
from django.utils import timezone
from django.http import HttpResponse

def home(request):

    name = request.user.username if request.user.is_authenticated else "GUEST"

    return render(request,"home.html",{"name":name})
    

def register(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            message ="user already existed"
        else:
            User.objects.create_user(username=username,password=password)
            message = "registration successfull"
    
    return render(request,"register.html",{"message":message})
        

def login_view(request):
    msg = " "
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request,username=username,password=password) #this creates a session

        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            msg = "invalid username or password"
    
    return render(request,"login.html",{"message":msg})


def logout_view(request):
    auth_logout(request)
    return redirect("home")


#for crud operation of book

def books_list(request):
    book = Book.objects.all()
    return render(request,"books_list.html",{"books":book})

def add_book(request):
    msg = " "

    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        isbn = request.POST.get("isbn")
        copies = request.POST.get("copies")


        if Book.objects.filter(isbn=isbn).exists():
            msg = "Book with this ISBN already exists"

        else:
            Book.objects.create(
                title=title,
                author=author,
                isbn=isbn,
                copies=int(copies),
                added_by=request.user if request.user.is_authenticated else None
            )
            return redirect('books_list')
    return render(request,"add_book.html",{"message":msg})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    message = ""
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.author = request.POST.get("author")
        book.isbn = request.POST.get("isbn")
        book.copies = int(request.POST.get("copies"))
        book.save()
        return redirect('books_list')

    return render(request, 'library/books/edit_book.html', {'book': book, 'message': message})

def delete_book(request,book_id):
    book = get_object_or_404(Book,id=book_id)
    book.delete()
    print("book deleted successfully")
    return redirect("books_list")


def borrow_book(request,book_id):
    if not request.user.is_authenticated:
        return redirect("login")
    
    book = get_object_or_404(Book,id=book_id)

    if book.copies > 100:
       return HttpResponse("No copies available to borrow!")

    if Borrow.objects.filter(user=request.user,book=book,returned=False).exists():
       return HttpResponse("you have already borrowed this book")

    Borrow.objects.create(user=request.user, book=book)
    book.copies -= 1
    book.save()
    return redirect('my_borrows')


def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id, user=request.user)
    if borrow.returned:
        return HttpResponse("Book already returned!")

    borrow.returned = True
    borrow.returned_at = timezone.now()
    borrow.save()

    book = borrow.book
    book.copies += 1
    book.save()

    return redirect('my_borrows')


def my_borrows(request):
    if not request.user.is_authenticated:
        return redirect('login')

    borrows = Borrow.objects.filter(user=request.user).order_by('-borrowed_at')
    return render(request, 'my_borrows.html', {'borrows': borrows})


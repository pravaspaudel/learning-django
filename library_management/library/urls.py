from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('books/', views.books_list, name='books_list'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),

   path('borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
   path('return/<int:borrow_id>/', views.return_book, name='return_book'),
   path('my-borrows/', views.my_borrows, name='my_borrows'), 

]
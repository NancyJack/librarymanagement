from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.template import loader
import io
import datetime
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

# Create your views here.
@login_required
def registerUser(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('library:main')
    context = {
        'form':form,

    }
    return render(request,'library/register.html',context)

@login_required
def displayUser(request):
    
    dis_user = User.objects.all().exclude(is_superuser=True) 
    groups = Group.objects.all()
    
    context = {
        'dis_user':dis_user,
        'groups':groups,
    }
    return render(request,'library/displayUser.html',context)

@login_required
def displaybookUser(request):
    displaybook = AddBook.objects.all() 
    
    context = {
        'displaybook':displaybook,

        
    }
    return render(request,'library/displaybookuser.html',context)

@login_required
def main(request):
    
 
    context ={
              
    }
    return render(request,'library/main.html',context)

@login_required
def addBook(request):
    
    if request.method == 'POST':
        form = AddBookForm(request.POST or None,request.FILES)
        if form.is_valid():  
            
            instance= form.save(commit=False)
            instance.save()  
            return redirect('library:displayBook')
    else:
        form = AddBookForm()
    return render(request,'library/add.html',{'form':form})

@login_required
def displayBook(request):
    display = AddBook.objects.all()
    context ={
        'display':display,

    }
    return render(request,'library/displaybook.html',context)

@login_required
def update(request,id):
    book = AddBook.objects.get(id=id)
    form = AddBookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid():
        edit = form.save(commit=False)
        edit.save()
        return redirect('library:displayBook')
    return render(request,'library/add.html',{'form':form})

@login_required
def delete_book(request,id):
    del_book = AddBook.objects.get(id=id)
    if request.method=='POST':
        del_book.delete()
        return redirect('library:displayBook')
    return render(request,'library/delete_book.html',{'del_book':del_book})

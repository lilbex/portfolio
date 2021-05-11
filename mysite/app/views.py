from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import Contacts

def index(request):
    form = Contacts()
    return render(request,'app/index.html',{'form': form})


def create(request):
    if request.method == 'POST':
        form = Contacts(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'app/index.html')
    form = Contacts()

    return render(request,'app/index.html',{'form': form})

# def insert_user_message(request):
#     email = request.POST('email')
#     message = request.POST('message')
#     user_info = PostForm(email=email, message=message)
#     user_info.save()
#     return render(request, 'app/index.html' messages =message)
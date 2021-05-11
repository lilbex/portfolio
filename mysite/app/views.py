from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .forms import PostForm

def index(request):
    return render(request, 'app/index.html')


def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = PostForm()

    return render(request,'app/index.html',{'form': form})

# def insert_user_message(request):
#     email = request.POST('email')
#     message = request.POST('message')
#     user_info = PostForm(email=email, message=message)
#     user_info.save()
#     return render(request, 'app/index.html' messages =message)
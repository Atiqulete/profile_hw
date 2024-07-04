from django.shortcuts import render
from .models import userInfo,Experience

# Create your views here.


def home(request):
    user_info = userInfo.objects.all()
    context = {
        'user_info' : user_info
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def projects(request):
    return render(request,'projects.html')


def resume(request):
    ex_info = Experience.objects.all()
    context = {
        'ex_info' : ex_info
    }
    return render(request,'resume.html',context,)


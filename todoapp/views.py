from django.shortcuts import render

# Create your views here.

def viewhtml(request):
    return render(request,'todoapp/index.html')

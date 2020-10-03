from django.shortcuts import render
from .models import todolist

# Create your views here.

def viewhtml(request):
    todo_items=todolist.objects.order_by('id')
    context={'todo_items':todo_items}
    return render(request,'todoapp/index.html',context)

from django.http.response import HttpResponse
from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect, HttpResponse
import datetime

# Create your views here.

def todo_view(request):
    all_items = TodoItem.objects.all()
    return render(request, "todo_app/todo_page.html", {"all_items": all_items})

def add_item(request):
    newItem = TodoItem(content = request.POST['content'])
    newItem.save()
    return HttpResponseRedirect("/todo/")

def remove_item(request, todo_id):
    delete_item = TodoItem.objects.get(id=todo_id)
    delete_item.delete()
    return HttpResponseRedirect("/todo/")


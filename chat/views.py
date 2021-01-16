from django.shortcuts import render
from django.http import JsonResponse
from .decorators import view_template

@view_template(template="chat/index.html")
def index(request):
    return JsonResponse({"title": "Django NO-SPA TODO"})

def loader(request):
    return render(request, "chat/loader.html", {})

@view_template(template="chat/todos.html")
def todos(request):
    todos = [{"name": "xx"}]
    return JsonResponse({"todos": todos})
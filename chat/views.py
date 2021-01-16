from django.shortcuts import render
from django.http import JsonResponse
from .decorators import view_template

@view_template(template="chat/index.html")
def index(request):
    items = [{"name": "Felix"}, {"name": "Ethan"}]
    return JsonResponse({"items": items})

def loader(request):
    return render(request, "chat/loader.html", {})

def other(request):
    return render(request, "chat/other.html", {})
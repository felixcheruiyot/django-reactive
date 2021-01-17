from django.shortcuts import render
from django.http import JsonResponse
import json

from .decorators import view_template


from .models import Todo

@view_template(template="chat/index.html")
def index(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))
            if not data["label"]:
                raise Exception("Label field is required")
            Todo.objects.create(label=data["label"])
        return JsonResponse({"title": "Django NO-SPA TODO"})
    except Exception as ex:
        return JsonResponse({"title": "Django NO-SPA TODO", "errors": str(ex)}, status=400)

@view_template(template="chat/form2.html")
def todos2(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))
            if not data["label"]:
                raise Exception("Label field is required")
            Todo.objects.create(label=data["label"])
        return JsonResponse({"title": "Django NO-SPA TODO"})
    except Exception as ex:
        return JsonResponse({"title": "Django NO-SPA TODO", "errors": str(ex)}, status=400)


def loader(request):
    return render(request, "chat/loader.html", {})

@view_template(template="chat/todos.html")
def todos(request):
    todos = Todo.objects.all()
    todos = [{"label": todo.label, "done": todo.done} for todo in todos]
    return JsonResponse({"todos": todos})
from functools import wraps
from django.template.loader import get_template
from django.http import HttpResponse


def view_template(template):
    def decorator(func):
        @wraps(func)
        def _wrapped(request, *args, **kwargs):
            if request.GET.get("format") == "template":   
                template_obj = get_template(template)  
                content = template_obj.template.source
                return HttpResponse(content=content)            
            return func(request, *args, **kwargs)
        return _wrapped
    return decorator
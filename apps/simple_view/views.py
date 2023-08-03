# from django.http import HttpResponse
from django.shortcuts import render


# My Django view
def index(request, name: str, age: int):
    # simple_message = f"Hello, {name}! My age {age}"
    simple_message = "Hello"
    # return HttpResponse(f"Hello, {name}! My age {age}")

    return render(
        request=request,
        template_name="generator/simple_list.html",
        context={"message": simple_message, "view_name": "simple_view"},
    )

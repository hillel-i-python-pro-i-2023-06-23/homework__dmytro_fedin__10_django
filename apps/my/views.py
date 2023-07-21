from django.http import HttpResponse


def index(request, name: str, age: int):
    return HttpResponse(f"Hello, {name}! I am {age}")

# from django.http import HttpResponse
from django.shortcuts import render


# My Django view
def index(request):
    simple_message = "hello"
    # return HttpResponse(f"Hello, {name}! My age {age}")

    return render(
        request=request,
        template_name="simple_view/simple_view.html",
        context={"simple_message": simple_message, "view_name": "simple_view"},
    )

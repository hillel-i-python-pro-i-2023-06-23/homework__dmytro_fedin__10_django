# from django.http import HttpResponse

from django.shortcuts import render


def generator(request):
    return render(
        request=request,
        template_name="index.html",  # :TODO: extend basic template
        context={"value": "Hello world"},
    )

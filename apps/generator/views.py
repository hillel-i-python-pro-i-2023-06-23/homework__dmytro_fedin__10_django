from django.shortcuts import render

from apps.generator.services import generate_users


# def generator(request):
#     return render(
#         request=request,
#         template_name="index.html",  # :TODO: extend basic template
#         context={"value": "Hello all"},
#     )


def generator(request):
    user_generator = generate_users()
    user_list = list(user_generator)

    return render(
        request=request,
        template_name="base/generator.html",  # :TODO: extend basic template
        context={"users": user_list},
    )

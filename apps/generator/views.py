from django.shortcuts import render

# Get model for data handling
from apps.generator.services import generate_users


def generator(request):
    user_generator = generate_users()
    user_list = list(user_generator)

    return render(
        request=request,
        template_name="base/generator.html",
        context={"users": user_list},
    )

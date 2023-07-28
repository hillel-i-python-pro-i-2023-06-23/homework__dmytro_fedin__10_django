from django.shortcuts import render

# Get model for data handling
from apps.generator.services import generate_users


def generator(request):
    user_generator = generate_users()

    # Avoid identical items in the sequence
    unique_user_set = set(user_generator)
    user_list = list(unique_user_set)

    return render(
        request=request,
        template_name="base/generator.html",
        context={"users": user_list},
    )

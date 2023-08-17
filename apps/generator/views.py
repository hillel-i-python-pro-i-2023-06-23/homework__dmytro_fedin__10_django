from django.shortcuts import render

# Get model for data handling
from apps.generator.services import generate_users


def generator(request, user_count):
    user_generator = generate_users(amount=user_count)

    # Avoid identical items in the sequence
    unique_user_set = set(user_generator)
    user_list = list(unique_user_set)

    return render(
        request=request,
        template_name="generator/simple_list.html",
        context={"users": user_list, "user_count": user_count},
    )

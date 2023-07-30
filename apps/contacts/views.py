# For Django
from django.shortcuts import render

# For contacts handling
from apps.contacts.services import generate_contacts


# Get model for data handling
def contacts(request):
    contacts_list = generate_contacts()

    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={"users": contacts_list},
    )

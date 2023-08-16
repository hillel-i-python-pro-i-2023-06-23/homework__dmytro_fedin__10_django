# For Django
from django.views.generic import ListView

from apps.contacts.models import Contact


# Get model for data handling
class ContactsListView(ListView):
    model = Contact
    # template_name = "contacts/contacts_list.html"

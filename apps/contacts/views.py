# For Django
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from apps.contacts.models import Contact


# Get views for CRUD using generic views
# List view
class ContactsListView(ListView):
    model = Contact


# Create contact view
# needs appropriate template contacts/contact_form.html
class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "phone_number"]
    # Address to place created instance
    success_url = reverse_lazy("contacts:contacts_list")

# For Django
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

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


class ContactUpdateView(UpdateView):
    model = Contact
    fields = ["name", "phone_number"]

    # Address to place created instance
    success_url = reverse_lazy("contacts:contacts_list")

    # Send data to template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class ContactDeleteView(DeleteView):
    model = Contact

    # Address to place created instance
    success_url = reverse_lazy("contacts:contacts_list")

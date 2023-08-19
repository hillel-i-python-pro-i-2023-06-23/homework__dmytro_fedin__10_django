# For Django
from django.views.generic import ListView

from apps.contacts.models import Contact


# View to show user list from database
class ContactsListView(ListView):
    model = Contact
    # template_name = "contacts/contacts_list.html"

from django.urls import path

# Import view from contacts app
from apps.contacts import views

app_name = "contacts"

# Route to show previously generated list in template
urlpatterns = [
    path("", views.ContactsListView.as_view(), name="contacts_list"),
]

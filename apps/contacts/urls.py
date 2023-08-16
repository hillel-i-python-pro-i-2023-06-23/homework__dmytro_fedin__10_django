from django.urls import path

# Import view from contacts app
from apps.contacts import views

app_name = "contacts"

# Add routes instead of using decorators in views
urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
]

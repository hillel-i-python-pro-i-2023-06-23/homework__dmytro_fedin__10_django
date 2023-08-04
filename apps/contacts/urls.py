from django.urls import path

# Import view from contacts app
from . import views

app_name = "contacts"

urlpatterns = [
    path("list/", views.ContactsListView.as_view(), name="contacts_list"),
    path("create/", views.ContactCreateView.as_view(), name="contacts_create"),
    path(
        "update/<int:pk>/",
        views.ContactUpdateView.as_view(),
        name="contacts_update",
    ),
    path(
        "delete/<int:pk>/",
        views.ContactDeleteView.as_view(),
        name="contacts_delete",
    ),
]

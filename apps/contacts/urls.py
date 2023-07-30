from django.urls import path

# Import view from contacts app
from apps.contacts import views

app_name = "generator"

# Add routes instead of using decorators in views
urlpatterns = [
    path("", views.contacts, name="value"),
]

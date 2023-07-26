from django.urls import path

# Import view from my app
from apps.generator import views

app_name = "generator"

# Add routes instead of using decorators in views
urlpatterns = [
    path(
        "", views.generator, name="value"
    ),  # :TODO: change direct link ("/my-app") to named link ("my_app:my_route")
]

from django.urls import path

# Import view from my app
from apps.generator import views

app_name = "my"

# Add routes instead of using decorators in views
urlpatterns = [
    path(
        "<name>/<int:age>/", views.index, name="Index"
    ),  # :TODO: change direct link ("/my-app") to named link ("my_app:my_route")
]

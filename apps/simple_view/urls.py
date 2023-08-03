from django.urls import path

# Import view from my app
from apps.simple_view import views

app_name = "simple_view"

# Add routes instead of using decorators in views
urlpatterns = [
    # path("<name>/<int:age>/", views.index, name="Index"),
    path("", views.index, name="simple_view")
]

from django.urls import path

# Import view from my app
from apps.generator import views

app_name = "generator"

# Add routes instead of using decorators in views
urlpatterns = [
    path("<int:user_count>/", views.generator, name="value"),
]

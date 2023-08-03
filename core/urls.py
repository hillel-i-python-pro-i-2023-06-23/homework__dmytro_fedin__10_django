from django.urls import path, include


# Add routes instead of using decorators in views
urlpatterns = [
    path("simple_view/", include("apps.simple_view.urls")),
    path("generator/", include("apps.generator.urls")),
    path("contacts/", include("apps.contacts.urls")),
]

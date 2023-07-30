from django.urls import path, include


# Add routes instead of using decorators in views
urlpatterns = [
    path("my/", include("apps.my.urls")),
    path("generator/", include("apps.generator.urls")),
    path("contacts/", include("apps.contacts.urls")),
]

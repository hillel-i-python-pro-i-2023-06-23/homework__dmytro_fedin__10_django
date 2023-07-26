from django.urls import path, include


# Add routes instead of using decorators in views
urlpatterns = [
    # Connect
    path("my/", include("apps.my.urls")),
    path("generator/", include("apps.generator.urls")),
]

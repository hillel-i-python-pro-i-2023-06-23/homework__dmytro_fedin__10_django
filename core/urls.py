from django.urls import path, include


# Add routes instead of using decorators in views
urlpatterns = [
    # Connect
    # path("", include("apps.base.urls")),
    path("my/", include("apps.my.urls")),
]

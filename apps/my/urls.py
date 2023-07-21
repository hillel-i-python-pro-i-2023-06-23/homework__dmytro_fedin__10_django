from django.urls import path
from . import views

app_name = "my"

# Add routes instead of using decorators in views
urlpatterns = [
    path("<name>/<int:age>/", views.index, name="Index"),
]

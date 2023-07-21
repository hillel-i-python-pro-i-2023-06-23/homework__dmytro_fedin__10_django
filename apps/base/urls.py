from django.urls import path
from . import views

app_name = 'base'

# Add routes instead of using decorators in views
urlpatterns = [
    path('', views.index, name='Index'),
]
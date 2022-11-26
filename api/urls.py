from django.urls import path
from . import views

# define paths
urlpatterns = [
    path('', views.endpoints )
]
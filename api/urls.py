from django.urls import path
from . import views

# define paths
urlpatterns = [
    path('', views.endpoints ),
    path('locations/', views.location_list, name='locations'),
    path('locations/<str:name>/', views.location_detail)
]
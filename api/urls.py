from django.urls import path
from . import views
from .views import location_detail

# define paths
urlpatterns = [
    path('', views.endpoints ),
    path('locations/', views.location_list, name='locations'),
    path('locations/<str:name>/', views.location_detail),
    path('/redirect/', location_detail),
    path('customers/', views.customer_lists)
]
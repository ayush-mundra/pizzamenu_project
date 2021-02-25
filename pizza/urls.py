
from django.urls import path
from pizza import views

urlpatterns = [
   path('type',views._pizzatype, name='type'),
    path('showall',views.showall, name='showall'),
    path('filter',views.filter, name='filter'),
]

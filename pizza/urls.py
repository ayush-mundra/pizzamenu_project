from django.urls import path
from pizza import views

urlpatterns = [
   path('type',views._pizzatype, name='type'),
    path('showall',views.showall, name='showall'),
    path('filter',views.filter, name='filter'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
]
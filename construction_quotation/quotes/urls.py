from django.urls import path
from .views import (
    request_quote,
    project_detail,
    home,
    material_list,
    add_material,
    edit_material,

)

urlpatterns = [
    path('', home, name='home'),  # Add this line for the home view
    path('request-quote/', request_quote, name='request_quote'),
    path('project/<int:project_id>/', project_detail, name='quote_detail'),
path('materials/', material_list, name='material_list'),
   path('materials/add/', add_material, name='add_material'),
   path('materials/edit/<int:material_id>/', edit_material, name='edit_material'),

]
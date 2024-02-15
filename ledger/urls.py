from django.urls import path 
from .views import recipes_list, recipe_1, recipe_2

urlpatterns = [
    path('list/', recipes_list, name='recipes'),
    path('1/', recipe_1, name='recipe'),
    path('2/', recipe_2, name='recipe'),
]

app_name = 'ledger'

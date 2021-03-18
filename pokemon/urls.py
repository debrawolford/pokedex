from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon, name="pokemon"),
    path('<int:pokemon_id>/', views.pokemon_details, name='pokemon_details'),
]
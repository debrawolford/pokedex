from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon, name="pokemon"),
    path('abilities/', views.abilities, name="abilities"),
    path('<int:pokemon_id>/', views.pokemon_details, name='pokemon_details'),
]
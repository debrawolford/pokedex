from django.contrib import admin
from .models import Pokemon, Ability

class AbilityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "effect"
    )

class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        "_id",
        "name",
        "height",
    )

    ordering = ("_id",)

admin.site.register(Ability, AbilityAdmin)
admin.site.register(Pokemon, PokemonAdmin)

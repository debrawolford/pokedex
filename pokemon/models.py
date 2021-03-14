from django.db import models

# Create your models here.
class Ability(models.Model):
    class Meta:
        verbose_name_plural = 'Abilities'
    
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    ability = models.ForeignKey('Ability', null=True, blank=True, on_delete=models.CASCADE)
    height = models.IntegerField()
    sprite_url = models.URLField(max_length=1024, null=True, blank=True)

def __str__(self):
        return self.name
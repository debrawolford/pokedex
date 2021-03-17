from django.db import models

# Create your models here.
class Ability(models.Model):
    class Meta:
        verbose_name_plural = 'Abilities'
    
    name = models.CharField(max_length=254, null=False, blank=False)
    effect = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    _id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=False, blank=False)
    height = models.IntegerField(null=False, blank=False)
    sprite = models.URLField(max_length=1024, null=True, blank=True)
    ability1 = models.CharField(max_length=200, null=True, blank=True)
    ability2 = models.CharField(max_length=200, null=True, blank=True)
    ability3 = models.CharField(max_length=200, null=True, blank=True)
    ability4 = models.CharField(max_length=200, null=True, blank=True)

def __str__(self):
        return self.name
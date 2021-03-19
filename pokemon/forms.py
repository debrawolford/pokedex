from django import forms
from .models import Pokemon


class PokemonForm(forms.ModelForm):

    class Meta:
        model = Pokemon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'input-field'
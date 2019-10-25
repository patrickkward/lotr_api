from django import forms

from .models import Films


class FilmForm(forms.ModelForm):
    class Meta:
            fields = ['film_name', 'nominations']

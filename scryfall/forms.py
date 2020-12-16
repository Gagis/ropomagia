from django import forms


class IDForm(forms.Form):
    """Form to take desired Scryfall ID from user input."""
    scryfall_id = forms.CharField(label='Scryfall ID', max_length=100)

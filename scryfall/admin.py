from django.contrib import admin

from .models import Card

# Jotta lisättyjä kortteja voisi poistaa tämän kautta.
admin.site.register(Card)

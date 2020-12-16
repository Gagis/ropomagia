from django.urls import path

from . import views

app_name = 'scryfall'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='lisää'),
    path('cards/', views.cards, name='listaa'),
]

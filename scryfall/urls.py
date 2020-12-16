from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='lisää'),
    path('cards', views.cards, name='listaa'),
]

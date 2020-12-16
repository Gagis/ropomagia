from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Card
from .forms import IDForm
from .api import fetch


def index(request):
    """Indexiä ei nyt käytetä mihinkään jännään."""
    return HttpResponse("Hei maailma! Kohta lisätään kortteja kantaan!")


def add(request):
    """Lisäysnäkymä joka kysyy käyttäjältä ID:tä, tarkistaa löytyykö sitä
    tietokannasta ja hakee Scryfallista vastaavan kortin tiedot jos ei löydy.
    """
    if request.method == 'POST':
        # Poimin tän rakenteen formien dokumentaatiosta, mutten tiedä, miksi
        # if POST ja else rakenne on relevantti
        form = IDForm(request.POST)

        if form.is_valid():
            input_id = form.cleaned_data['scryfall_id']
            if Card.objects.filter(scryfall_id=input_id).exists():
                error = 'Kortti on jo tietokannassa.'

            else:
                card = fetch(input_id)
                Card(name=card['name'],
                     set_name=card['set_name'],
                     collector_number=card['collector_number'],
                     scryfall_id=card['scryfall_id'],
                     ).save()

            return HttpResponseRedirect('add/')

    else:
        form = IDForm()

    return render(request, 'scryfall/add.html', {'form': form})


def cards(request):
    card_list = Card.objects.order_by('set_name', 'collector_number')
    context = {'card_list': card_list}
    return render(request, 'scryfall/cards.html', context)

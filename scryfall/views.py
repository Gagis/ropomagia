from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from .models import Card
from .forms import IDForm

def index(request):
    return HttpResponse("Hei maailma! Kohta lisätään kortteja kantaan!")

def add(request):
    if request.method == 'POST':
        form = IDForm(request.POST)
        if form.is_valid():
            input_id = form.cleaned_data['scryfall_id']
            return HttpResponseRedirect('cards/')

    else:
        form = IDForm()

    return render(request, 'scryfall/add.html', {'form': form})

def cards(request):
    card_list = Card.objects.order_by('set', 'collector_number')
    context = {'card_list': card_list}
    return render(request, 'scryfall/cards.html', context)

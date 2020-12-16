from django.db import models

class Card(models.Model):
    name = models.CharField('Card Name', max_length=200)
    set = models.CharField('Set Name', max_length=200)
    collector_number = models.IntegerField('Collector Number')
    scryfall_id = models.CharField('Scryfall ID', max_length=200)

    def __str__(self):
        return self.name

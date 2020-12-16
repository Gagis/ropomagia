import requests


def fetch(scryfall_id):
    """Gets the data of a card matching scryfall_id from Scryfall's API and
    returns its name, set, collector number and ID as a dictionary.
    """
    r = requests.get('https://api.scryfall.com/cards/' + scryfall_id).json()
    return {'name': r['name'],
            'set_name': r['set_name'],
            'collector_number': r['collector_number'],
            'scryfall_id': r['id'],
            }

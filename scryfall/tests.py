from django.test import TestCase

from .api import fetch


class ApiTests(TestCase):

    def test_fetch_returns_known_test_card(self):
        thalia = {'name': 'Thalia, Guardian of Thraben',
                  'set_name': 'Masters 25',
                  'collector_number': '36',
                  'scryfall_id': '97ff44c9-6ff5-432d-9876-488c96833c39'}
        self.assertDictEqual(fetch('97ff44c9-6ff5-432d-9876-488c96833c39'),
                             thalia)

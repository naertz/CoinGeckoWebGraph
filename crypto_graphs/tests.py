from django.test import TestCase

from . import views

# Create your tests here.


class ViewsTestCase(TestCase):
    def test_load_views(self):
        request = self.client.request()
        atari_response = views.atari_view(request)
        bitcoin_response = views.bitcoin_view(request)
        bitcoin_cash_response = views.bitcoin_cash_view(request)
        curve_dao_token_response = views.curve_dao_token_view(request)
        ethereum_response = views.ethereum_view(request)
        fantom_response = views.fantom_view(request)
        monero_response = views.monero_view(request)
        tarot_response = views.tarot_view(request)
        tomb_response = views.tomb_view(request)
        self.assertEqual(atari_response.status_code, 200)
        self.assertEqual(bitcoin_response.status_code, 200)
        self.assertEqual(bitcoin_cash_response.status_code, 200)
        self.assertEqual(curve_dao_token_response.status_code, 200)
        self.assertEqual(ethereum_response.status_code, 200)
        self.assertEqual(fantom_response.status_code, 200)
        self.assertEqual(monero_response.status_code, 200)
        self.assertEqual(tarot_response.status_code, 200)
        self.assertEqual(tomb_response.status_code, 200)

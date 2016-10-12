import unittest
from coral_client import Client
import base64

search_params = {'checkin': '2017-01-28', 'checkout': '2017-01-30', 'pax': '1',
                 'destination_code': '11260', 'client_nationality': 'tr',
                 'currency': 'USD'}

search_params2 = {'checkin': '2017-02-23', 'checkout': '2017-02-25',
                  'pax': '1',
                  'destination_code': '11260', 'client_nationality': 'tr',
                  'currency': 'USD'}

a = Client(base64.b64decode('Z29raGFuLmthcmFib2dh'),
           base64.b64decode('WWV0MTIzKys='))

product_code = a.search(search_params)[1]['results'][0]['products'][0][
    'code']
product_code2 = a.search(search_params2)[1]['results'][0]['products'][0][
    'code']


class TestClass(unittest.TestCase):
    search_response = a.search(search_params)
    availability_response = a.availability(product_code)
    provision_response = a.provision(product_code)

    def test_search(self):
        self.assertEqual(self.search_response[0], 200)
        self.assertGreater(int(self.search_response[1]['count']), 0)
        self.assertIsInstance(self.search_response[1], dict)
        self.assertIsInstance(self.search_response[1]['results'], list)
        self.assertIn('results', self.search_response[1])

    def test_availability(self):
        self.assertEqual(self.availability_response[0], 200)
        self.assertTrue(
            isinstance(self.availability_response[1]['rooms'], list))
        self.assertGreater(float(self.availability_response[1]['price']), 0)

    def test_provision(self):
        self.assertEqual(self.provision_response[0], 200)
        self.assertIn('rooms', self.provision_response[1])
        self.assertIsNot(self.provision_response[1]['currency'], 'null')

    def test_book(self):
        book_code = self.provision_response[1]['code']
        book_response = a.book(book_code)
        self.assertEqual(book_response[0], 200)
        self.assertDictContainsSubset({'pay_at_hotel': False},
                                      book_response[1])

    def test_cancel(self):
        book_code2 = a.provision(product_code2)[1]['code']
        cancel_code = a.book(book_code2)[1]['code']
        cancel_response = a.cancel(cancel_code)
        self.assertEqual(cancel_response
                         [0], 200)
        self.assertEqual(cancel_response[2].headers['allow'], 'POST, OPTIONS')

    def test_bookings(self):
        self.assertEqual(a.bookings()[0], 200)


if __name__ == "__main__":
    unittest.main()

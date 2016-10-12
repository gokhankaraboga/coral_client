import unittest
from coral_client import Client
import base64

search_params = {'checkin': '2016-11-25', 'checkout': '2016-12-14', 'pax': '1',
                 'destination_code': '1c11e', 'client_nationality': 'tr',
                 'currency': 'USD'}

search_params2 = {'checkin': '2016-12-25', 'checkout': '2016-12-27',
                  'pax': '1',
                  'destination_code': '1c11e', 'client_nationality': 'tr',
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
    book_code = provision_response[1]['code']
    book_response = a.book(book_code)

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

    def test_provision(self):
        self.assertEqual(self.provision_response[0], 200)

    def test_book(self):
        self.assertEqual(self.book_response[0], 200)

    def test_cancel(self):
        book_code = a.provision(product_code2)[1]['code']
        cancel_code = a.book(book_code)[1]['code']
        self.assertEqual(a.cancel(cancel_code)
                         [0], 200)

    def test_bookings(self):
        self.assertEqual(a.bookings()[0], 200)


if __name__ == "__main__":
    unittest.main()

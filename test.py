import unittest
from coral_client import Client

search_params = {'checkin': '2017-01-28', 'checkout': '2017-01-30', 'pax': '1',
                 'destination_code': '14bc7', 'client_nationality': 'tr',
                 'currency': 'USD'}

search_params2 = {'checkin': '2017-02-23', 'checkout': '2017-02-25',
                  'pax': '1',
                  'destination_code': '14bc7', 'client_nationality': 'tr',
                  'currency': 'USD'}

wrong_params = {'checkin': '2016-11-11', 'checkout': '2016-11-15',
                'pax': '1',
                'destination_code': '14bc7xyz', 'client_nationality': 'tr',
                'currency': 'USD'}
'''
In order to test search method with wrong parameters. There is no such
destination code as above.
'''

a = Client('username', 'password')
'''Please enter your own login credentials'''

search_response = a.search(search_params)
search_response2 = a.search(search_params2)

product_code = search_response[1]['results'][0]['products'][0][
    'code']
product_code2 = search_response2[1]['results'][0]['products'][0][
    'code']


class TestClass(unittest.TestCase):
    availability_response = a.availability(product_code)
    provision_response = a.provision(product_code)
    bookings_response = a.bookings()

    def __init__(self, *args, **kwargs):
        super(TestClass, self).__init__(*args, **kwargs)

    def test_search(self):
        self.assertEqual(search_response[0], 200)
        self.assertGreater(int(search_response[1]['count']), 0)
        self.assertIsInstance(search_response[1], dict)
        self.assertIsInstance(search_response[1]['results'], list)
        self.assertIn('results', search_response[1])

        '''Failed test case'''
        with self.assertRaisesRegexp(ValueError, 'error_code'):
            a.search(wrong_params)

    def test_availability(self):
        self.assertEqual(self.availability_response[0], 200)
        self.assertTrue(
            isinstance(self.availability_response[1]['rooms'], list))
        self.assertGreater(float(self.availability_response[1]['price']), 0)

        '''Failed test case'''
        with self.assertRaises(TypeError):
            a.availability()

    def test_provision(self):
        self.assertEqual(self.provision_response[0], 200)
        self.assertIn('rooms', self.provision_response[1])
        self.assertIsNot(self.provision_response[1]['currency'], 'null')

        '''Failed test case'''
        with self.assertRaises(TypeError):
            a.provision({wrong_params})

    def test_book(self):
        book_code = self.provision_response[1]['code']
        book_response = a.book(book_code)

        self.assertEqual(book_response[0], 200)
        self.assertDictContainsSubset({'pay_at_hotel': False},
                                      book_response[1])
        self.assertEqual(book_response[2].headers['vary'], 'Accept')

        '''Failed test case'''
        with self.assertRaises(TypeError):
            a.book()

    def test_cancel(self):
        book_code2 = a.provision(product_code2)[1]['code']
        cancel_code = a.book(book_code2)[1]['code']
        cancel_response = a.cancel(cancel_code)

        self.assertEqual(cancel_response
                         [0], 200)
        self.assertEqual(cancel_response[2].headers['allow'], 'POST, OPTIONS')

        '''Failed test case'''
        with self.assertRaises(ValueError):
            a.cancel('1ABCDEFGH')

    def test_bookings(self):
        self.assertEqual(self.bookings_response[0], 200)
        self.assertEqual(self.bookings_response[2].headers['content-type'],
                         'application/json')
        self.assertIsInstance(self.bookings_response[1], list)

        '''Failed test case'''
        with self.assertRaises(TypeError):
            a.bookings(product_code)


if __name__ == "__main__":
    unittest.main()

import requests
from urlparse import urljoin


class Client(object):
    def __init__(self, username, password):
        self.BASE_URL = 'http://localhost:8000/api/v2/'
        self.SEARCH_URL = urljoin(self.BASE_URL, 'search/')
        self.AVAILABILITY_URL = urljoin(self.BASE_URL, 'availability/')
        self.PROVISION_URL = urljoin(self.BASE_URL, 'provision/')
        self.BOOK_URL = urljoin(self.BASE_URL, 'book/')
        self.CANCEL_URL = urljoin(self.BASE_URL, 'cancel/')
        self.BOOKINGS_URL = urljoin(self.BASE_URL, 'bookings/')

        self.username = username
        self.password = password

        self.s = requests.Session()
        self.s.auth = (self.username, self.password)

    def search(self, search_params):
        response = self.s.get(self.SEARCH_URL, params=search_params)
        if response.status_code != 200:
            raise ValueError(response.json())
        return response.status_code, response.json()

    def availability(self, product_code):
        response = self.s.get(self.AVAILABILITY_URL + product_code)

        if response.status_code != 200:
            raise ValueError(response.json())
        return response.status_code, response.json()

    def provision(self, product_code):
        response = self.s.post(self.PROVISION_URL + product_code)

        if response.status_code != 200:
            # return response.json()
            raise ValueError(response.json())

        return response.status_code, response.json(), response

    def book(self, provision_code, book_params):
        response = self.s.post(self.BOOK_URL + provision_code,
                               data=book_params)
        if response.status_code != 200:
            raise ValueError(response.json())
            # return response.json()

        return response.status_code, response.json(), response

    def cancel(self, book_code):
        response = self.s.post(self.CANCEL_URL + book_code)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.status_code, response.json(), response

    def bookings(self):
        response = self.s.get(self.BOOKINGS_URL)

        if response.status_code != 200:
            raise ValueError(response.json())

        return response.status_code, response.json(), response

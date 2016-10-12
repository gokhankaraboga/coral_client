from coral_client import Client
import base64

'''
seach-availability-provision-book-cancel-bookings
provision, book ve cancel post yapar
search, availability ve bookings get yapar
'''

search_params = {'checkin': '2016-11-25', 'checkout': '2016-12-14', 'pax': '1',
                 'destination_code': '11260', 'client_nationality': 'tr',
                 'currency': 'USD'}

a = Client(base64.b64decode('Z29raGFuLmthcmFib2dh'),
           base64.b64decode('WWV0MTIzKys='))

response_1 = a.search(search_params)
product_code = response_1[1]['results'][0]['products'][0]['code']
print '\n', 'product code:', product_code
print 'search json object:', response_1, '\n'

response_2 = a.availability(product_code)
print 'Availability json object:', response_2, '\n'

response_3 = a.provision(product_code)
book_code = response_3[1]["code"]
print 'book code:', book_code

response_4 = a.book(book_code)
cancel_code = response_4[1]['code']
print 'book json object:', response_4, '\n'
print 'cancel code:', cancel_code

response_5 = a.cancel(cancel_code)
print 'cancel json object:', response_5, '\n'

response_6 = a.bookings()
print 'bookings json object:', response_6

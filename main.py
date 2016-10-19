from coral_client import Client
import datetime

'''
seach-availability-provision-book-cancel-bookings
provision, book and cancel ----> POST
search, availability and bookings ----> GET
'''

checkin_date = datetime.datetime.now() + datetime.timedelta(2 * 365 / 12)
checkout_date = datetime.datetime.now() + datetime.timedelta(2.5 * 365 / 12)
'''
Checkin and Checkout dates are automatically assigned two and 2.5 months from
the current day respectively
'''

checkin_param = '{0}-{1}-{2}'.format(checkin_date.year, checkin_date.month,
                                     checkin_date.day)

checkout_param = '{0}-{1}-{2}'.format(checkout_date.year, checkout_date.month,
                                      checkout_date.day)

search_params = {'checkin': checkin_param, 'checkout': checkout_param,
                 'pax': '1',
                 'destination_code': '11260', 'client_nationality': 'tr',
                 'currency': 'USD'}

book_params = {'name': '1,Gokhan,Karaboga,adult'}

a = Client('username', 'password')
'''Please enter your own login credentials'''

response_1 = a.search(search_params)
product_code = response_1[1]['results'][0]['products'][0]['code']
print '\n', 'product code:', product_code
print 'search json object:', response_1, '\n'

response_2 = a.availability(product_code)
print 'Availability json object:', response_2, '\n'

response_3 = a.provision(product_code)
book_code = response_3[1]["code"]
print 'book code:', book_code

response_4 = a.book(book_code, book_params)
cancel_code = response_4[1]['code']
print 'book json object:', response_4, '\n'
print 'cancel code:', cancel_code

response_5 = a.cancel(cancel_code)
print 'cancel json object:', response_5, '\n'

response_6 = a.bookings()
print 'bookings json object:', response_6

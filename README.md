# README #



#### INTRODUCTION ####

    * This project is basically a python client library for Hotelspro product.
    
    * Version: 1.0.0
    
    * More detailed info at [https://bitbucket.org/gokhankaraboga/project1_coral_client/overview]

#### INSTALLATION ####

    $ python setup.py install

#### USAGE ####

    In order to be able to use the library, please add the line below to
    your code
    
    * from coral_client import Client
    
### EXAMPLES : search(), availability(), provision(), book(), cancel() ###
``` python
    from coral_client import Client

    '''
    seach-availability-provision-book-cancel-bookings
    provision, book and cancel ----> POST
    search, availability and bookings ----> GET
    '''
    
    search_params = {'checkin': '2016-11-25', 'checkout': '2016-12-14', 'pax': '1',
                     'destination_code': '11260', 'client_nationality': 'tr',
                     'currency': 'USD'}
    
    a = Client(username, password)
    
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
```
    

#### RESPONSE ####

    * Search Response

    HTTP 200 OK
    Content-Type: application/json
    Vary: Accept
    Allow: OPTIONS, GET

``` javascript
    
    {
        "count": 68, 
        "code": "a1674071f7f84ed58df7d886e8437932", 
        "next_page_code": null, 
        "results": [
            {
                "hotel_code": "101000", 
                "checkout": "2016-10-22", 
                "checkin": "2016-10-20", 
                "destination_code": "20b17", 
                "products": [
                    {
                        "code": "EBAAIVQRIAAAAAAAAAAAAAAAAAAAAAAAAAHAoWdAcff4TtWN99iG6EN5MoAAAAAAAAAAAAAAAAPVgAAAAAPVgAEKgIoC_nXpXtMCAAIAAAAAAAAAAAAABA", 
                        "list_price": "43.62", 
                        "offer": true, 
                        "pay_at_hotel": false, 
                        "price": "39.26", 
                        "currency": "EUR", 
                        "cost": "39.26", 
                        "rooms": [
                            {
                                "pax": {
                                    "adult_quantity": 1, 
                                    "children_ages": []
                                }, 
                                "room_category": "Standard", 
                                "room_description": "Leisure Standard + Breakfast", 
                                "room_type": "SB"
                            }
                        ], 
                        "nonrefundable": null, 
                        "providers": [
                            "tourico"
                        ], 
                        "supports_cancellation": true, 
                        "hotel_currency": null, 
                        "hotel_price": null, 
                        "meal_type": "BE", 
                        "policies": [], 
                        "minimum_selling_price": null, 
                        "view": false
                    }, 
                    {
                        "code": "EBAAIVQRIAAAAAAAAAAAAAAAAAAAAAAAAAHAoWdAcff4TtWN99iG6EN5MoAAAAAAAAAAAAAAAARCgAAAAARCgAEKgHnCu3vfKQkGABIAAAAAAAAAAAAABA", 
                        "list_price": "43.62", 
                        "offer": false, 
                        "pay_at_hotel": false, 
                        "price": "43.62", 
                        "currency": "EUR", 
                        "cost": "43.62", 
                        "rooms": [
                            {
                                "pax": {
                                    "adult_quantity": 1, 
                                    "children_ages": []
                                }, 
                                "room_category": "Standard", 
                                "room_description": "Standard + Breakfast", 
                                "room_type": "SB"
                            }
                        ], 
                        "nonrefundable": null, 
                        "providers": [
                            "tourico"
                        ], 
                        "supports_cancellation": true, 
                        "hotel_currency": null, 
                        "hotel_price": null, 
                        "meal_type": "BE", 
                        "policies": [], 
                        "minimum_selling_price": null, 
                        "view": false
                    }, 
                    {
                        "code": "EBAAIVQRIAAAAAAAAAAAAAAAAAAAAAAAAAHAoWdAcff4TtWN99iG6EN5MoAAAAAAAAAAAAAAAAPVgAAAAAPVoAEKgADPw6srRn5yACIAAAAAAAAAAAAABA", 
                        "list_price": "43.62", 
                        "offer": true, 
                        "pay_at_hotel": false, 
                        "price": "39.26", 
                        "currency": "EUR", 
                        "cost": "39.26", 
                        "rooms": [
                            {
                                "pax": {
                                    "adult_quantity": 1, 
                                    "children_ages": []
                                }, 
                                "room_category": "Standard", 
                                "room_description": "Non Refundable Standard + Breakfast", 
                                "room_type": "SB"
                            }
                        ], 
                        "nonrefundable": true, 
                        "providers": [
                            "tourico"
                        ], 
                        "supports_cancellation": true, 
                        "hotel_currency": null, 
                        "hotel_price": null, 
                        "meal_type": "BE", 
                        "policies": [], 
                        "minimum_selling_price": null, 
                        "view": false
                    }
                ]
            }, 
```

#### TESTS ####
    Every function on the client library is tested under various test cases.
    Availability unit test component can be seen below as a sample. Other
    components are to be found at test.py file.
    
    def test_availability(self):
    self.assertEqual(self.availability_response[0], 200)
    self.assertTrue(
        isinstance(self.availability_response[1]['rooms'], list))
    self.assertGreater(float(self.availability_response[1]['price']), 0)

    '''Failed test case'''
    with self.assertRaises(TypeError):
        a.availability()
    

#### LICENSE ####

    This project is licenced as public license. Further information can be
    found on LİCENSE file.
# Created by: Kay Lin
# Created on: 2nd-Nov-2017
# Created for: ICS3U
# This program displays address

def address(streetAddress, city = '', province = '', postalCode = '', apartmentNumber = ''):
    # address info
    
    if apartmentNumber == '':
       print(streetAddress + ' ' + city + ' ' + province + ' ' + postalCode)
    else:
       print(streetAddress + ' ' + city + ' ' + province + ' ' + postalCode + ' ' + apartmentNumber)

street_address = raw_input("Enter street address: ")
city_name = raw_input("Enter your city name: ")
province_name = raw_input("Enter your province name: ")
postal_code = raw_input("Enter postal code: ")
apartment_address = raw_input("Do you have apartment number(y/n): ")
if apartment_address == 'y':
    apartment_number = raw_input("Enter your apartment number: ")
    address(street_address, city = city_name, province = province_name, postalCode = postal_code, apartmentNumber = apartment_number )
else:
    address(street_address, city = city_name, province = province_name, postalCode = postal_code)

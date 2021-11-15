"""
Hello Dear coach :)
The first part of the program (Add information and Edit) ---> Line 7 ta 721
The second part (search) ---> 941 to 960 (Inside the menu)
The third part (class Transaction) ---> 775 to 800
"""
import math
import csv , sys
class Address:
    list_address = []
    def __init__(self, name_city, name_street, number_plates, postal_code):
        self.name_city = name_city
        self.name_street = name_street
        self.number_plates = int(number_plates)
        self.postal_code = int(postal_code)

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_address(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        while True:
            try:
                number_plates = int(input("number plates :"))
                if not isinstance(number_plates, int):  #check the int
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                postal_code = int(input("postal code :"))
                if not isinstance(postal_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        id = (name_city, name_street, number_plates, postal_code)
        cls.list_address.append(id)
        return (name_city, name_street, number_plates, postal_code)

    def edit_address(self):
        self.name_city = input("name city: ")
        self.name_street = input("name street :")
        while True:
            try:
                self.number_plates = int(input("number plates :"))
                if not isinstance(self.number_plates, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                self.postal_code = int(input("postal code :"))
                if not isinstance(self.postal_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        id = Address.generate_id(self.name_city, self.name_street, self.number_plates, self.postal_code)
        if id in Address.list_address:
            print("The editing operation was not performed correctly")
        else:
            Address.list_address.clear()
            Address.list_address.append(id)
        print(f"Home address successfully edited")

    def show_adrdress(self):
        return f"Address home is : City :{self.name_city} , street :{self.name_street},\n" \
               f"number plates :{self.number_plates} , postal code :{self.postal_code}"
class Person:
    list_person = []
    def __init__(self, f_name, l_name, number_phon, email_address, national_code):
        self.f_name = f_name
        self.l_name = l_name
        self.email_address = email_address
        self.nathional_code = int(national_code)
        self.number_phon = int(number_phon)

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_person(cls):
        f_name = input("First name: ")
        l_name = input("Last name :")
        while True:
            try:
                number_phon = int(input("number phone :"))
                if not isinstance(number_phon, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        email_address = input("Email :")
        while not cls.check_email(email_address):
            email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        while True:
            try:
                national_code = int(input("national_Code :"))
                if not isinstance(national_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while not cls.check_national_code(national_code):
            national_code = int(input("The national_Code is incorrect, Must be 10 digits. please enter again :"))
        id = cls.generate_id(f_name, l_name, number_phon, email_address)
        cls.list_person.append(id)
        return cls(f_name=f_name, l_name=l_name, number_phon=number_phon, email_address=email_address, national_code=national_code)

    @staticmethod
    def check_email(email):
        if '@' in email:
            if '.com' == email[-4:]:
                return True
        else:
            return False

    @staticmethod
    def check_national_code(national_Code):  # check the national code 10 digits
        digits = int(math.log10(national_Code)) + 1
        if digits == 10:
            return True
        else:
            return False

    def edit_profile(self):
        self.f_name = input("First name: ")
        self.l_name = input("Last name :")
        while True:
            try:
                self.number_phon = int(input("number phone :"))
                if not isinstance(self.number_phon, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        self.email_address = input("Email :")
        while not self.check_email(self.email_address):
            self.email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        while True:
            try:
                self.national_code = int(input("national_Code :"))
                if not isinstance(self.national_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while not self.check_national_code(self.national_code):
            self.national_code = int(input("The national_Code is incorrect, Must be 10 digits. please enter again :"))
        id = Person.generate_id(self.f_name, self.l_name, self.number_phon, self.email_address, self.nathional_code)
        if id in Person.list_person:
            print("The editing operation was not performed correctly")
        else:
            Person.list_person.clear()
            Person.list_person.append(id)
        print(f"Profile  successfully edited , new profile is : First name :{self.f_name} \n"
              f",last name :{self.l_name}, email address :{self.email_address}, nathional_code :{self.nathional_code}\n"
              f", number phone :{self.number_phon}")

    def __str__(self):
        return f"Information {self.f_name} {self.l_name} was recorded"


class Apartment(Address):
    list_attributsApartment = []
    def __init__(self,  number_room, floor,number_floor,area,name_city, name_street, number_plates, postal_code,\
                 phone_status, Mortgage_amount, rent_amount,seling_price, parking, Type):
        super(Apartment, self).__init__(name_city, name_street, number_plates, postal_code)
        self.area = int(area)
        self.number_room = int(number_room)
        self.floor = int(floor)
        self.number_floor = int(number_floor)
        self.phone_status = phone_status
        self.Mortgage_amount = int(Mortgage_amount)
        self.rent_amount = int(rent_amount)
        self.seling_price = int(seling_price)
        self.parking = parking
        self.Type = Type

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_attributs_apartment(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        while True:
            try:
                number_plates = int(input("number plates :"))
                if not isinstance(number_plates, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                postal_code = int(input("postal code :"))
                if not isinstance(postal_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                number_floor = int(input("How many floors? "))
                if not isinstance(number_floor, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                floor = int(input("floor :"))
                if not isinstance(floor, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                number_room = int(input("How many room? "))
                if not isinstance(number_room, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                area = int(input("Area :"))
                if not isinstance(area, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        phone_status = input("phone status ? Active / InActive :")
        parking = input("parking ?! yes / no :")
        Type = input("rate or sale:")
        while True:
            try:
                seling_price = int(input("seling_price : ***Please leave this amount 0 if the property is for rent !"))
                if not isinstance(seling_price, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                Mortgage_amount = int(input("Mortgage_amount : ***Please leave this amount 0 if the property is for sale !"))
                if not isinstance(Mortgage_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                rent_amount = int(input("rent_amount : ***Please leave this amount 0 if the property is for sale !"))
                if not isinstance(rent_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        id = Apartment.generate_id(number_room, floor, number_floor, phone_status, Mortgage_amount, rent_amount,
                                seling_price,seling_price, parking, name_city, name_street, number_plates, postal_code, Type)
        cls.list_attributsApartment.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code,
                   number_floor=number_floor, parking=parking, floor=floor, number_room=number_floor,
                   area=area, phone_status=phone_status, Mortgage_amount=Mortgage_amount,
                   rent_amount=rent_amount, seling_price=seling_price, Type=Type)

    def edit_information_apartment(self):
       while True:
           try:
               self.number_room = int(input("number_room :"))
               if not isinstance(self.number_room, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       while True:
           try:
               self.floor = int(input("floor :"))
               if not isinstance(self.floor, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       while True:
           try:
               self.number_floor = int(input("number_floor"))
               if not isinstance(self.number_floor, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       while True:
           try:
               self.area = int(input("Area :"))
               if not isinstance(self.area, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       self.parking = input("parking? yes or no ! :")
       self.phone_status = input("phone_status ")
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
           while True:
               try:
                   self.seling_price = int(input("seling_price :"))
                   if not isinstance(self.seling_price, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
       else:
           self.Type = 'rate'
           while True:
               try:
                   self.Mortgage_amount = int(input("Mortgage_amount :"))
                   if not isinstance(self.Mortgage_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
           while True:
               try:
                   self.rent_amount = int(input("rent_amount :"))
                   if not isinstance(self.rent_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')

       id = Apartment.generate_id(self.number_room, self.floor, self.number_floor,
        self.phone_status, self.Mortgage_amount, self.rent_amount, self.seling_price, self.seling_price, self.parking,
        self.name_city, self.name_street, self.number_plates, self.postal_code, self.Type, self.area)
       if id in Apartment.list_attributsApartment:
            print("The editing operation was not performed correctly")
       else:
            Apartment.list_attributsApartment.clear()
            Apartment.list_attributsApartment.append(id)
       print("Apartment_home information successfully edited")

    def __str__(self):
        return (f"View home information : City :{self.name_city} ,street :{self.name_street} \'"
              f",umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f", number floor :{self.number_floor}, parking :{self.parking}, floor :{self.floor}, number room :{self.number_room} \'"
              f", phone status :{self.phone_status} ,area :{self.area}  Mortgage_amount :{self.Mortgage_amount}, rent_amount :{self.rent_amount} \'"
              f", seling_price :{self.seling_price},  Type is:{self.Type}")

    def file_aparteman(self):

        with open('aparteman2.csv', 'a', newline='') as csvfile:
            fieldnames = ['name_city', 'name_street', 'number_plates', 'postal_code', 'number_floor', 'parking', 'floor',
                          'number_room', 'phone_status', 'area', 'Mortgage_amount', 'rent_amount', 'seling_price', 'Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name_city': self.name_city, 'name_street':self.name_street, 'number_plates':self.number_plates,
                             'postal_code':self.postal_code, 'number_floor':self.number_floor, 'parking':self.parking,
                             'floor':self.floor, 'number_room':self.number_room, 'phone_status':self.phone_status, 'area':self.area,
                             'Mortgage_amount':self.Mortgage_amount, 'rent_amount':self.rent_amount, 'seling_price':self.seling_price, 'Type':self.Type})



class Home(Apartment,Address):
    list_attributsHome = []
    def __init__(self,name_city, name_street, number_plates, postal_code, number_room,  area, phone_status,
                 Mortgage_amount, rent_amount, seling_price, Type, number_floor, yard_area, parking, floor):
        super(Home, self).__init__(number_room,  area, phone_status, Mortgage_amount, rent_amount, seling_price,
                                   Type, number_floor, parking, floor, name_city, name_street, number_plates, postal_code)

        self.yard_area = int(yard_area)

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_attributs_Home(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        while True:
            try:
                number_plates = int(input("number plates :"))
                if not isinstance(number_plates, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                postal_code = int(input("postal code :"))
                if not isinstance(postal_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                number_floor = int(input("How many floors? "))
                if not isinstance(number_floor, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                number_room = int(input("How many room? "))
                if not isinstance(number_room, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                area = int(input("Area :"))
                if not isinstance(area, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                yard_area = int(input("yard_area :"))
                if not isinstance(yard_area, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        phone_status = input("phone status . Active / Inactive :")
        Type = input("sale or rent :")
        while True:
            try:
                seling_price = int(input("seling_price : ***Please leave this amount None if the property is for rent !"))
                if not isinstance(seling_price, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')

        while True:
            try:
                Mortgage_amount = int(input("Mortgage_amount : ***Please leave this amount None if the property is for sale !"))
                if not isinstance(Mortgage_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                rent_amount = int(input("rent_amount : ***Please leave this amount None if the property is for sale !"))
                if not isinstance(rent_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        parking = None
        floor = None
        id = Home.generate_id(number_room, number_floor, phone_status, Mortgage_amount, rent_amount,
                seling_price, name_city, name_street, number_plates, postal_code, yard_area, area, Type, parking, floor)
        cls.list_attributsHome.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code,
                   number_floor=number_floor,  number_room=number_floor, yard_area= yard_area,
                   area=area, phone_status=phone_status, Mortgage_amount=Mortgage_amount,
                   rent_amount=rent_amount, seling_price=seling_price, Type=Type, parking=parking, floor=floor)

    def edit_information_Home(self):
       while True:
           try:
               self.number_room = int(input("number_room :"))
               if not isinstance(self.number_room, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       while True:
           try:
               self.number_floor = int(input("number_floor"))
               if not isinstance(self.number_floor, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       self.phone_status = input("phone status . Active / Inactive : ")
       while True:
           try:
               self.yard_area = int(input(" yard_area :"))
               if not isinstance(self.yard_area, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       while True:
           try:
               self.area = int(input(" area :"))
               if not isinstance(self.area, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
           while True:
               try:
                   self.seling_price = int(input("seling_price :"))
                   if not isinstance(self.seling_price, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
       else:
           self.Type = 'rate'
           while True:
               try:
                   self.Mortgage_amount = int(input("Mortgage_amount :"))
                   if not isinstance(self.Mortgage_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
           while True:
               try:
                   self.rent_amount = int(input("rent_amount :"))
                   if not isinstance(self.rent_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
       self.parking = None
       self.floor = None
       id = Home.generate_id(self.number_room, self.number_floor, self.phone_status, self.Mortgage_amount,
          self.rent_amount, self.seling_price, self.name_city
        , self.name_street, self.number_plates, self.postal_code, self.yard_area, self.area, self.Type, self.parking, self.floor)
       if id in Home.list_attributsHome:
            print("The editing operation was not performed correctly")
       else:
            Home.list_attributsHome.clear()
            Home.list_attributsHome.append(id)
       print("Apartment_home information successfully edited")

    def __str__(self):
        return(f"View home information : City :{self.name_city} ,street :{self.name_street} \'"
              f",umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f", number floor :{self.number_floor},  yard area :{self.yard_area}, area :{self.area}, number room :{self.number_room} \'"
              f", phone status :{self.phone_status} ,  Mortgage_amount :{self.Mortgage_amount}, rent_amount :{self.rent_amount} \'"
              f", seling_price :{self.seling_price} , Type is:{self.Type} ")

    def file_Home(self):
        with open('Home1.csv', 'a', newline='') as csvfile2:
            fieldnames = ['name_city', 'name_street', 'number_plates', 'postal_code', 'number_floor', 'yard_area', 'area',
                          'number_room', 'phone_status', 'Mortgage_amount', 'rent_amount', 'seling_price', 'Type']
            writer = csv.DictWriter(csvfile2, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name_city': self.name_city, 'name_street':self.name_street, 'number_plates':self.number_plates,
                             'postal_code':self.postal_code, 'number_floor':self.number_floor, 'yard_area':self.yard_area,
                             'area':self.area, 'number_room':self.number_room, 'phone_status':self.phone_status,
                             'Mortgage_amount':self.Mortgage_amount, 'rent_amount':self.rent_amount, 'seling_price':self.seling_price, 'Type':self.Type})

class Shope(Home,Apartment,Address):
    list_attributsShop = []
    def __init__(self,name_city, name_street, number_plates, postal_code, phone_status, Mortgage_amount, rent_amount,
                 seling_price, Type, area, number_floor, yard_area, parking, number_room):
        super(Shope, self).__init__(self,name_city, name_street, number_plates, postal_code, number_room,  area,
                                    phone_status, Mortgage_amount, rent_amount, seling_price, Type, number_floor,
                                    yard_area, parking)

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_attributs_shop(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        while True:
            try:
                number_plates = int(input("number plates :"))
                if not isinstance(number_plates, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                postal_code = int(input("postal code :"))
                if not isinstance(postal_code, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        phone_status = input("phone status . Active / Inactive :")
        while True:
            try:
                area = int(input("Area :"))
                if not isinstance(area, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        Type = input("sale or rate:")
        while True:
            try:
                seling_price = int(input("seling_price :"))
                if not isinstance(seling_price, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                Mortgage_amount = int(input("Mortgage_amount :"))
                if not isinstance(Mortgage_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')
        while True:
            try:
                rent_amount = int(input("rent_amount :"))
                if not isinstance(rent_amount, int):
                    raise TypeError("Oops!  That was no valid number.  Try again...")
                else:
                    break
            except (TypeError, ValueError):
                print('Oops!  That was no valid number.  Try again...')

        parking = None
        number_floor = None
        number_room = None
        yard_area = None
        #floor = None
        id = Shope.generate_id(area, phone_status, Mortgage_amount, rent_amount,
        seling_price, name_city, name_street, number_plates, postal_code, Type, number_floor, yard_area, parking, number_room)
        cls.list_attributsShop.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code,
        phone_status=phone_status, area=area,  Mortgage_amount=Mortgage_amount, rent_amount=rent_amount, seling_price=seling_price
        , Type=Type, number_floor=number_floor, yard_area=yard_area, parking=parking, number_room=number_room)


    def edit_information_shop(self):
       self.phone_status = input("phone status . Active / Inactive : ")
       while True:
           try:
               self.area = int(input(" area :"))
               if not isinstance(self.area, int):
                   raise TypeError("Oops!  That was no valid number.  Try again...")
               else:
                   break
           except (TypeError, ValueError):
               print('Oops!  That was no valid number.  Try again...')
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
           while True:
               try:
                   self.seling_price = int(input("seling_price :"))
                   if not isinstance(self.seling_price, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
       else:
           self.Type = 'rate'
           while True:
               try:
                   self.Mortgage_amount = int(input("Mortgage_amount :"))
                   if not isinstance(self.Mortgage_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
           while True:
               try:
                   self.rent_amount = int(input("rent_amount :"))
                   if not isinstance(self.rent_amount, int):
                       raise TypeError("Oops!  That was no valid number.  Try again...")
                   else:
                       break
               except (TypeError, ValueError):
                   print('Oops!  That was no valid number.  Try again...')
       self.parking = None
       #self.floor = None
       self.number_floor = None
       self.number_room = None
       self.yard_area = None
       id = Shope.generate_id(self.area,self.phone_status, self.Mortgage_amount, self.rent_amount, self.seling_price,\
        self.name_city, self.name_street, self.number_plates, self.postal_code, self.Type, self.parking,
        self.floor, self.number_room, self.yard_area)

       if id in Shope.list_attributsShop:
            print("The editing operation was not performed correctly")
       else:
            Shope.list_attributsShop.clear()
            Shope.list_attributsShop.append(id)
       print("Apartment_home information successfully edited ")

    def __str__(self):
        print(f"View home information : City :{self.name_city} ,street :{self.name_street}\'"
              f"umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f" area :{self.area}, phone status :{self.phone_status}, Mortgage_amount :{self.Mortgage_amount}\'"
              f" rent_amount :{self.rent_amount}, seling_price :{self.seling_price} , Type is:{self.Type} ")

    def file_shope(self):
        with open('Shope1.csv', 'a', newline='') as csvfile3:
            fieldnames = ['name_city', 'name_street', 'number_plates', 'postal_code', 'area',
                         'phone_status', 'Mortgage_amount', 'rent_amount', 'seling_price', 'Type']
            writer = csv.DictWriter(csvfile3, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'name_city': self.name_city, 'name_street':self.name_street, 'number_plates':self.number_plates,
                             'postal_code':self.postal_code, 'area':self.area, 'phone_status':self.phone_status,
                             'Mortgage_amount':self.Mortgage_amount, 'rent_amount':self.rent_amount, 'seling_price':self.seling_price, 'Type':self.Type})

class Transaction:
    def __init__(self, buyer, owner, date_of_contract, expiration_date, status_active=True):
        #property is activated first, and deactivated after sale
        self.buyer = buyer
        self.owner = owner
        self.date_of_contract = date_of_contract
        self.expiration_date = expiration_date
        self.status_active = status_active

    def type(self, a): # a is correct teype
        self.t = input('Enter the type you want :')
        self.a = a
        if self.t == self.a:
            print('correct')
        else:
            print("I'm sorry !")

    def active_status(self):
        if not self.status_active:
            self.status_active = False
        else:
            print(f"The {self.status_active} is {self.status_active}")
        return True

    def __str__(self):
        if self.status_active == False:
            return f"Property Mr or Miss {self.owner} to Mr or Miss {self.buyer} granted."


list_Sorce_aparteman = []
dict_aprtement = {}
list_Sorce_home = []
dict_home = {}
list_Sorce_shope = []
dict_shope = {}
while True:
    menu1 = input("""\n1.Add\n2.search\n3.Transaction\n4.Exite\nWhich number ? """)
    if menu1 == '1':
        menu2 = input("""\n1.Apartment\n2.home\n3.shop\nWhich number ? """)
        if menu2 == '1':
            print("Please fill out the form below")
            menu01 = input("""\n1.Owner\n2.Tenate\n? """)
            if menu01 == '1':
                print("*** Owner ***")
                Owner = Person.add_person()
                dict_aprtement.update({'Owner': Owner})
                print(Owner.__dict__)
                while True:
                    menu3 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu3 == '1':
                        Owner.edit_profile()
                    if menu3 == '2':
                        break
                print(f"information {Owner} is correct ")
            if menu01 == '2':
                print("***  Tenant ***")
                Tenant = Person.add_person()
                dict_aprtement.update({'Tenate': Tenant})
                with open('aparteman1.csv', 'a') as csvfile:
                    fields = ['Tenate']
                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writerow({'Tenate': Tenant})
                while True:
                    menu4 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu4 == '1':
                        Tenant.edit_profile()
                    if menu4 == '2':
                        break
                print(f"information {Tenant} is correct ")

            print("*** Apartment information ***")
            apartment = Apartment.add_attributs_apartment()
            dict_aprtement.update({'apartemaent': apartment})
            list_Sorce_aparteman.append(dict_aprtement)
            while True:
                menu4 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                if menu4 == '1':
                    apartment.edit_address()
                    apartment.edit_information_apartment()
                    apartment.__str__()
                if menu4 == '2':
                    break
            apartment.file_aparteman()

        if menu2 == '2':
            menu02 = input("""\n1.Owner\n2.Tenate\n? """)
            if menu02 == '1':
                print("Please fill out the form below")
                print("*** Owner ***")
                Owner = Person.add_person()
                dict_home.update({'Owner': Owner})
                print(Owner.__dict__)
                while True:
                    menu5 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu5 == '1':
                        Owner.edit_profile()
                    if menu5 == '2':
                        break
                print(f"information {Owner} is correct ")
            if menu02 == '2':
                print("***  Tenant ***")
                Tenant = Person.add_person()
                dict_home.update({'Tenate': Tenant})
                while True:
                    menu6 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu6 == '1':
                        Tenant.edit_profile()
                    if menu6 == '2':
                        break
                print(f"information {Tenant} is correct ")
            print("*** Home information ***")
            home = Home.add_attributs_Home()
            dict_home.update({'Home': home})
            list_Sorce_home.append(dict_home)
            while True:
                menu7 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                if menu7 == '1':
                    home.edit_address()
                    home.edit_information_Home()
                if menu7 == '2':
                    break
            home.__str__()
            home.file_Home()

        if menu2 == '3':
            menu03 = input("""\n1.Owner\n2.Tenate\n? """)
            if menu03 == '1':
                print("Please fill out the form below")
                print("*** Owner ***")
                Owner = Person.add_person()
                dict_shope.update({'Owner': Owner})
                print(Owner.__dict__)
                while True:
                    menu8 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu8 == '1':
                        Owner.edit_profile()
                    if menu8 == '2':
                        break
                print(f"information {Owner} is correct ")
            if menu03 == '2':
                print("***  Tenant ***")
                Tenant = Person.add_person()
                dict_shope.update({'Tenate': Tenant})
                while True:
                    menu9 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                    if menu9 == '1':
                        Tenant.edit_profile()
                    if menu9 == '2':
                        break
                print(f"information {Tenant} is correct ")

            print("*** shope information ***")
            shop = Shope.add_attributs_shop()
            dict_shope.update({'Shope': shop})
            list_Sorce_shope.append(dict_shope)
            while True:
                menu10 = input("""Do you want to edit the information ?\n1.Yes\n2.No\nWhich number ?""")
                if menu10 == '1':
                    shop.edit_address()
                    shop.edit_information_shop()
                if menu10 == '2':
                    break
            shop.__str__()
            shop.file_shope()
    if menu1 == '2':
        menu11 = input("""serch information ---> 1.sale or rate , 2.area , 3.Mortgage_amount/rent_amount/seling_price
        \n1.Apartment\n2.home\n3.shop\nWhich number ? """)
        if menu11 == '1':
            filename = 'aparteman2.csv'
            with open(filename, newline='') as f:
                reader = csv.DictReader(f)
                try:
                    for row in reader:
                        print(row['Type'], row['area'], row['Mortgage_amount'], row['rent_amount'], row['seling_price'])
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

        elif menu11 == '2':
            filename = 'Home1.csv'
            with open(filename, newline='') as f:
                reader = csv.DictReader(f)
                try:
                    for row in reader:
                        print(row['Type'],row['area'], row['Mortgage_amount'], row['rent_amount'], row['seling_price'])
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

        elif menu11 == '3':
            filename = 'Shope1.csv'
            with open(filename, newline='') as f:
                reader = csv.DictReader(f)
                try:
                    for row in reader:
                        print(row['Type'], row['area'], row['Mortgage_amount'], row['rent_amount'], row['seling_price'])
                except csv.Error as e:
                    sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))

    if menu1 == '3':
        while True:
            menu12 = input("""\n1.Submit_Transaction\n2.cancle""")
            if menu12 == '1':
                print(list_Sorce_aparteman)
                date_contract = input("please enter date of contract")
                expiration_of_date = input("please enter expiration date")
                owner = Person.add_person()
                Tenant = Person.add_person()
                Contract = Transaction(owner, Tenant, date_contract, expiration_of_date)

            Contract.active_status()
            Contract.__str__()

    if menu1 == '4':
        break

print("just test for git")
print("for first branch")
print("for first branch")



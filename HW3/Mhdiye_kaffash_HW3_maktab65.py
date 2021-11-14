class Address:
    list_address = []
    def __init__(self, name_city, name_street, number_plates, postal_code):
        self.name_city = name_city
        self.name_street = name_street
        self.number_plates = number_plates
        self.postal_code = postal_code

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_address(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        number_plates = input("number plates :")
        postal_code = input("postal code :")
        id = (name_city, name_street, number_plates, postal_code)
        cls.list_address.append(id)
        return (name_city, name_street, number_plates, postal_code)

    def edit_address(self):
        self.name_city = input("name city: ")
        self.name_street = input("name street :")
        self.number_plates = input("number plates :")
        self.postal_code = input("postal code :")
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
        self.nathional_code = national_code
        self.number_phon = number_phon

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_person(cls):
        f_name = input("First name: ")
        l_name = input("Last name :")
        number_phon = input("number phone :")
        email_address = input("Email :")
        while not cls.check_email(email_address):
            email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        national_code = input("national_Code :")
        while not cls.check_national_code(national_code):
            national_code = input("The national_Code is incorrect, Must be 10 digits. please enter again :")
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
    def check_national_code(national_Code):
        if len(national_Code) == 10:
            return True
        else:
            return False

    def edit_profile(self):
        self.f_name = input("First name: ")
        self.l_name = input("Last name :")
        self.number_phon = input("number phone :")
        self.email_address = input("Email :")
        while not self.check_email(self.email_address):
            self.email_address = input("The address email is incorrect, put '@' in the email. Please enter again :")
        self.national_code = input("national_Code :")
        while not self.check_national_code(self.national_code):
            self.national_code = input("The national_Code is incorrect, Must be 10 digits. please enter again :")
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
        self.area = area
        self.number_room = number_room
        self.floor = floor
        self.number_floor = number_floor
        self.phone_status = phone_status
        self.Mortgage_amount = Mortgage_amount
        self.rent_amount = rent_amount
        self.seling_price = seling_price
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
        number_plates = input("number plates :")
        postal_code = input("postal code :")
        number_floor = input("How many floors? ")
        parking = input("parking ?! yes / no :")
        floor = input("floor :")
        number_room = input("How many room? ")
        area = input("Area :")
        phone_status = input("phone status . Active / Inactive :")
        Mortgage_amount = input("Mortgage_amount :")
        rent_amount = input("rent_amount :")
        seling_price = input("seling_price :")
        menu_type = input("""\n1.Sale\n2.rent\n? """)
        if menu_type == '1':
            Type = 'Sale'
        else:
            Type = 'rate'
        id = Apartment.generate_id(number_room, floor, number_floor, phone_status, Mortgage_amount, rent_amount,\
                                seling_price,seling_price, parking, name_city, name_street, number_plates, postal_code, Type)
        cls.list_attributsApartment.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code, \
                   number_floor=number_floor, parking=parking, floor=floor, number_room=number_floor,\
                   area=area, phone_status=phone_status, Mortgage_amount=Mortgage_amount, \
                   rent_amount=rent_amount, seling_price=seling_price, Type=Type)

    def edit_information_apartment(self):
       self.number_room = input("number_room :")
       self.floor = input("floor :")
       self.number_floor = input("number_floor")
       self.phone_status = input("phone_status ")
       self.Mortgage_amount = input("Mortgage_amount :")
       self.rent_amount = input("rent_amount :")
       self.seling_price = input("seling_price :")
       self.parking = input("parking :")
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
       else:
           self.Type = 'rate'
       id = Apartment.generate_id(self.number_room, self.floor, self.number_floor,\
        self.phone_status, self.Mortgage_amount, self.rent_amount, self.seling_price, self.seling_price, self.parking,\
        self.name_city, self.name_street, self.number_plates, self.postal_code, self.Type)
       if id in Apartment.list_attributsApartment:
            print("The editing operation was not performed correctly")
       else:
            Apartment.list_attributsApartment.clear()
            Apartment.list_attributsApartment.append(id)
       print("Apartment_home information successfully edited")

    def show_information_Apartment(self):
        print(f"View home information : City :{self.name_city} ,street :{self.name_street} \'"
              f",umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f", number floor :{self.number_floor}, parking :{self.parking}, floor :{self.floor}, number room :{self.number_room} \'"
              f", phone status :{self.phone_status} ,  Mortgage_amount :{self.Mortgage_amount}, rent_amount :{self.rent_amount} \'"
              f", seling_price :{self.seling_price},  Type is:{self.Type}")

class Home(Apartment,Address):
    list_attributsHome = []
    def __init__(self,name_city, name_street, number_plates, postal_code, number_room,  area, phone_status,\
                 Mortgage_amount, rent_amount, seling_price, Type, number_floor, yard_area, parking, floor):
        super(Home, self).__init__(number_room,  area, phone_status, Mortgage_amount, rent_amount, seling_price,\
                                   Type, number_floor, parking, floor,name_city, name_street, number_plates, postal_code)
        #super(Home, self).__init__()
        self.yard_area = yard_area

    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_attributs_Home(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        number_plates = input("number plates :")
        postal_code = input("postal code :")
        number_floor = input("How many floors? ")
        number_room = input("How many room? ")
        area = input("Area :")
        yard_area = input("yard_area :")
        phone_status = input("phone status . Active / Inactive :")
        Mortgage_amount = input("Mortgage_amount :")
        rent_amount = input("rent_amount :")
        seling_price = input("seling_price :")
        menu_type = input("""\n1.Sale\n2.rent\n?""")
        if menu_type == '1':
            Type = 'Sale'
        else:
            Type = 'rate'
        parking = None
        floor = None
        id = Home.generate_id(number_room, number_floor, phone_status, Mortgage_amount, rent_amount,\
                seling_price, name_city, name_street, number_plates, postal_code, yard_area, area, Type, parking, floor)
        cls.list_attributsHome.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code,\
                   number_floor=number_floor,  number_room=number_floor, yard_area= yard_area,\
                   area=area, phone_status=phone_status, Mortgage_amount=Mortgage_amount, \
                   rent_amount=rent_amount, seling_price=seling_price, Type=Type, parking=parking, floor=floor)

    def edit_information_Home(self):
       self.number_room = input("number_room :")
       self.number_floor = input("number_floor")
       self.phone_status = input("phone status . Active / Inactive : ")
       self.Mortgage_amount = input("Mortgage_amount :")
       self.rent_amount = input("rent_amount :")
       self.seling_price = input("seling_price :")
       self.yard_area = input(" yard_area :")
       self.area = input(" area :")
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
       else:
           self.Type = 'rate'
       self.parking = None
       self.floor = None
       id = Home.generate_id(self.number_room, self.number_floor, self.phone_status, self.Mortgage_amount,\
          self.rent_amount, self.seling_price, self.name_city\
        , self.name_street, self.number_plates, self.postal_code, self.yard_area, self.area, self.Type, self.parking, self.floor)
       if id in Home.list_attributsHome:
            print("The editing operation was not performed correctly")
       else:
            Home.list_attributsHome.clear()
            Home.list_attributsHome.append(id)
       print("Apartment_home information successfully edited")

    def show_information_Home(self):
        print(f"View home information : City :{self.name_city} ,street :{self.name_street} \'"
              f",umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f", number floor :{self.number_floor},  yard area :{self.yard_area}, area :{self.area}, number room :{self.number_room} \'"
              f", phone status :{self.phone_status} ,  Mortgage_amount :{self.Mortgage_amount}, rent_amount :{self.rent_amount} \'"
              f", seling_price :{self.seling_price} , Type is:{self.Type} ")

class Shope(Home):
    list_attributsShop = []
    def __init__(self,name_city, name_street, number_plates, postal_code, phone_status, Mortgage_amount, rent_amount,\
                 seling_price, Type, area, number_floor, yard_area, parking, number_room):
        super(Shope, self).__init__(self,name_city, name_street, number_plates, postal_code, number_room,  area,\
                                    phone_status, Mortgage_amount, rent_amount, seling_price, Type, number_floor,\
                                    yard_area, parking)



    @staticmethod
    def generate_id(*args):
        args = list(args)
        return args

    @classmethod
    def add_attributs_shop(cls):
        name_city = input("name city: ")
        name_street = input("name street :")
        number_plates = input("number plates :")
        postal_code = input("postal code :")
        area = input("Area :")
        phone_status = input("phone status . Active / Inactive :")
        Mortgage_amount = input("Mortgage_amount :")
        rent_amount = input("rent_amount :")
        seling_price = input("seling_price :")
        menu_type = input("""\n1.Sale\n2.rent\n? """)
        if menu_type == '1':
            Type = 'Sale'
        else:
            Type = 'rate'
        parking = None
        number_floor = None
        number_room = None
        yard_area = None
        #floor = None
        id = Shope.generate_id(area, phone_status, Mortgage_amount, rent_amount,\
        seling_price, name_city, name_street, number_plates, postal_code, Type, number_floor, yard_area, parking, number_room)
        cls.list_attributsShop.append(id)
        return cls(name_city=name_city, name_street=name_street, number_plates=number_plates, postal_code=postal_code,\
        phone_status=phone_status, area=area,  Mortgage_amount=Mortgage_amount, rent_amount=rent_amount, seling_price=seling_price\
        , Type=Type, number_floor=number_floor, yard_area=yard_area, parking=parking, number_room=number_room)

    def edit_information_shop(self):
       self.phone_status = input("phone status . Active / Inactive : ")
       self.Mortgage_amount = input("Mortgage_amount :")
       self.rent_amount = input("rent_amount :")
       self.seling_price = input("seling_price :")
       self.area = input(" area :")
       menu_type = input("""\n1.Sale\n2.rent\n? """)
       if menu_type == '1':
           self.Type = 'Sale'
       else:
           self.Type = 'rate'
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

    def show_information_shop(self):
        print(f"View home information : City :{self.name_city} ,street :{self.name_street}\'"
              f"umber plates :{self.number_plates} , postal code :{self.postal_code}\'"
              f" area :{self.area}, phone status :{self.phone_status}, Mortgage_amount :{self.Mortgage_amount}\'"
              f" rent_amount :{self.rent_amount}, seling_price :{self.seling_price} , Type is:{self.Type} ")

#-----------------------------------------------

list_Sorce_aparteman = []
dict_aprtement = {}
list_Sorce_home = []
dict_home = {}
list_Sorce_shope = []
dict_shope = {}
while True:
    menu1 = input("""\n1.Add\n2.Exite\nWhich number ? """)
    if menu1 == '1':
        menu2 = input("""\n1.Apartment\n2.home\n3.shop\nWhich number ? """)
        if menu2 == '1':
            print("Please fill out the form below")
            menu01 = input("""\n1.Owner\n2.Tenate\n? """)
            if menu01 == '1':
                print("*** Owner ***")
                Owner = Person.add_person()
                dict_aprtement.update({'Owner':Owner})
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

                if menu4 == '2':
                    break
            apartment.show_information_Apartment()
            print(list_Sorce_aparteman)

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
            home.show_information_Home()
            print(list_Sorce_home)

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
            shop.show_information_shop()
            print(list_Sorce_shope)
    if menu1 == '2':
        break

#------- Part2

class Real_Estate:
    def __init__(self):
        pass

    def type_sale(self):
        for i in len(list_Sorce_aparteman):
            if list_Sorce_aparteman[i]['apartemaent'].Type == 'sale':
                print(list_Sorce_aparteman[i])

    def type_rent(self):
        for i in len(list_Sorce_aparteman):
            if list_Sorce_aparteman[i]['apartemaent'].Type == 'rent':
                print(list_Sorce_aparteman[i])

    def area_ap(self):
        for i in len(list_Sorce_aparteman):
            print(list_Sorce_aparteman[i]['apartemaent'].area)

    def mortgage_amount_ap(self):
        for i in len(list_Sorce_aparteman):
            print(list_Sorce_aparteman[i]['apartemaent'].Mortgage_amount)

    def rent_amount_ap(self):
        for i in len(list_Sorce_aparteman):
            print(list_Sorce_aparteman[i]['apartemaent'].rent_amount)

    def seling_price_ap(self):
        for i in len(list_Sorce_aparteman):
            print(list_Sorce_aparteman[i]['apartemaent'].seling_price)

    def type_sale_h(self):
        for i in len(list_Sorce_home):
            if list_Sorce_home[i]['Home'].Type == 'sale':
                print(list_Sorce_home[i])

    def type_rent_h(self):
        for i in len(list_Sorce_home):
            if list_Sorce_home[i]['Home'].Type == 'rent':
                print(list_Sorce_home[i])

    def area_h(self):
        for i in len(list_Sorce_home):
            print(list_Sorce_home[i]['Home'].area)

    def mortgage_amount_h(self):
        for i in len(list_Sorce_home):
            print(list_Sorce_home[i]['Home'].Mortgage_amount)

    def rent_amount_h(self):
        for i in len(list_Sorce_home):
            print(list_Sorce_home[i]['Home'].rent_amount)

    def seling_price_h(self):
        for i in len(list_Sorce_home):
            print(list_Sorce_home[i]['Home'].seling_price)

    def type_sale_sh(self):
        for i in len(list_Sorce_shope):
            if list_Sorce_shope[i]['Shope'].Type == 'sale':
                print(list_Sorce_shope[i])

    def type_rent_sh(self):
        for i in len(list_Sorce_shope):
            if list_Sorce_shope[i]['Shope'].Type == 'rent':
                print(list_Sorce_shope[i])

    def area_sh(self):
        for i in len(list_Sorce_shope):
            print(list_Sorce_shope[i]['Shope'].area)

    def mortgage_amount_sh(self):
        for i in len(list_Sorce_shope):
            print(list_Sorce_aparteman[i]['Shope'].Mortgage_amount)

    def rent_amount_sh(self):
        for i in len(list_Sorce_shope):
            print(list_Sorce_shope[i]['Shope'].rent_amount)

    def seling_price_sh(self):
        for i in len(list_Sorce_shope):
            print(list_Sorce_shope[i]['Shope'].seling_price)


while True:
    menu02 = input("""\n1.Sales\n2.Rent\n3.area\n4.Mortgage amount\n5.Rent amount\n6.seling_price""")
    if menu02 == '1':
        menu02_1 = input("""\n1.Apartment\n2.Home\n3.Shope""")
        if menu02_1 == '1':
            Real_Estate.type_sale()
        if menu02_1 == '2':
            Real_Estate.type_sale_h()
        if menu02_1 == '3':
            Real_Estate.type_sale_sh()
    if menu02 == '7':
        break

    # if menu02 == '2':
    #     menu02_1 = input("""\n1.Apartment\n2.Home\n3.Shope""")
    #     if menu02_1 == '1':
    #         Real_Estate.type_sale()
    #     if menu02_1 == '2':
    #         Real_Estate.type_sale_h()
    #     if menu02_1 == '3':
    #         Real_Estate.type_sale_sh()



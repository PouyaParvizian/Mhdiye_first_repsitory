class Card_metro:
    cnt1 = 7
    users_list1 = []
    users_list2 = []
    list2_2 = []
    users_list3 = []
    def __init__(self, first_name, last_name, Expiration_date):
        self.first_name = first_name
        self.last_name = last_name
        self.Name = f'{self.first_name} {self.last_name}'
        #self.Expiration_date = Expiration_date

    def __repr__(self):
        return f"name: {self.name}"

    @classmethod
    def single_trip(cls):
        f_name = input('Fist name :')
        l_name = input('Last name :')
        #Name = f'{f_name} {l_name}'
        #id1 = Card_metro.cnt1 + 1
        id1 = Card_metro.generate_id(f_name, l_name)
        #Card_metro.cnt1 += 1
        #Card_metro.item1.update({Name: id1})
        #print(f"Single trip card with number id : {id1} has taken by {Name}")
        if id1 in Card_metro.users_list1:
             print('You are only allowed to use this card once')
        else:
             print(f"Single trip card has taken by {id1}")
             Card_metro.users_list1.append(id1)

    @classmethod
    def credit_card(cls):
        f_name = input('First name :')
        l_name = input('Last name :')
        id2 = Card_metro.generate_id(f_name, l_name)
        #return id2
        # Card_metro.users_list2.append(id2)
        # Card_metro.list2_2 = list(set(Card_metro.users_list2))
        for i in range(7):
            if id2 in Card_metro.users_list2:
                Card_metro.cnt1 -= 1
        if Card_metro.cnt1 == 0:
            print('Card expired')
        else:
            print(f"credit_card card has taken by {id2}")
            Card_metro.users_list2.append(id2)

    @staticmethod
    def generate_id(str1, str2):
        return f'{str1.lower()}_{str2.lower()}'

while True:
    menu = input("""
    1_single_trip card 
    2_credit card 
    3-Credit / time card
    4_ Exite
     ? :""")

    if menu == '1':
        userx = Card_metro.single_trip()

        # if userx.single_trip() in Card_metro.user_list:
        #     print('You are only allowed to use this card once')
        # else:
        #     print(f"Single trip card has taken by {userx}")
        #     Card_metro.users_list.append(userx)

    if menu == '2':
        userx = Card_metro.credit_card()


        # Card_metro.users_list2.append(userx)
        # Card_metro.list2_2 = list(set(Card_metro.users_list2))
        # for i in range(len(Card_metro.list2_2)):
        #     for j in range(len(Card_metro.users_list2)):
        #         if j == i:
        #             Card_metro.cnt1 += 1
        # if Card_metro.cnt1 >= 7:
        #     print('Card expired')
        # else:
        #     print(f"credit_card card has taken by {userx}")
        #     Card_metro.users_list2.append(userx)



    if menu == '4':
        break



#---------------------------------------------------------------------
class single_trip_Ticket:

    @staticmethod
    def use():
     falg = True
        if flag = True:
            print("you can't use it")
        else:
            flag = True


#-------------------------------------------------------------------------------------------
class Ticket:
    counter = 0
    def __init__(self ,validity_duration, validity_times):
        self.validity_duration = validity_duration
        self.validity_times = validity_times
        self.id = Ticket.counter + 1
        Ticket.counter += 1

    def __repr__(self):
        return f'card with id {self.id} Was registered'

    @classmethod
    def single_tripe(cls):
        flag = False
        # if flag == True:
        #     print("you can't use this card")
        # else:
        #     falg == True
        #     print("you use this ticket succes")
        return flag



class single_tripe(Ticket):
        def __init__(self, flag=False):
            self.flag = flag
            if bool(self.flag):
                print("you can't use this card")
            else:
                self.falg = True
                print("you use this ticket succes")


class credit_card(Ticket):







 while True:
    menu = input("""
    1_single_trip card 
    2_credit card 
    3-Credit / time card
    4_ Exite
     ? :""")
    if menu == '1':
        use = single_tripe()
        use = False



    if menu == '4':
        break




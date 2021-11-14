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
    cnt = 0
    def __init__(self, flag=False):
    self.flag = flag
    cnt += 1
    
        if self.flag == True:
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

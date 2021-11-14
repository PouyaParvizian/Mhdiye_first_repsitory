import time

class SingleTripe_card:
    i = 0
    def __init__(self):
        if SingleTripe_card.i == 0:
            print("The use of the card was successful")
            SingleTripe_card.i += 1
        elif SingleTripe_card.i > 0:
            print("you can'nt use This card")

class Credit_card :
    credit = 7
    def __init__(self):
        if Credit_card.credit > 0:
            print("The use of the card was successful")
            Credit_card.credit -= 1
            print(f"you can use this card {Credit_card.credit} more times.")
            user = input("Do you want to charge the card? 1.yes / 2.no ? ")
            if user == '1':
                Credit_card.credit += 10
                print(f"your credit_card is {Credit_card.credit}")
            if user == '2':
                print(f"Ok ! you can use this card {Credit_card.credit} more times.")
        elif Credit_card.credit == 0:
            print("End of card credit")

class Credit_time:
    credit = 10
    time = time.localtime()  #ba farakhani in mazhol zaman sodor kart moshkhas mishvad ( modate etebar kart ro 10 roz migirim)
    def __init__(self):
        print(f"This card was issued on {Credit_time.time} date .Card validity is up to 10 more days. ")
        #while Credit_time.time.tm_mday + 10:
        if Credit_time.credit > 0:
            print("The use of the card was successful")
            Credit_time.credit -= 1
            print(f"you can use this card {Credit_time.credit} more times.")
        elif Credit_time.credit == 0:
            print("End of card credit")

        if Credit_time.credit == 7 & Credit_time.time.tm_mday == Credit_time.time.tm_mday + 11:
            print(f"The card is valid 7 times, but the card has expired")


while True:

    menu = print("""
     1.single_trip card 
     2.credit card 
     3.Credit / time card
     4. No thing
    """)
    massage_menu = int(input("Choose a number :"))
    if massage_menu == 1:
        SingleTripe_card()
    if massage_menu == 2:
        Credit_card()
    if massage_menu == 3:
        Credit_time()
    elif massage_menu == 4:
        break


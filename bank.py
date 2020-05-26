import random 
import string
import pdb

numbers = list(string.digits)
capital_letters = list(string.ascii_uppercase)
l_com = numbers + capital_letters

class Bank:
    def __init__(self):
        self.cards = []

    def addCards(self, card):
        self.cards.append(card)
        print('Add card successfully!!!!')

    def checkExistingCard(self,l_card, name, acc_num):
        for item in l_card:
            if item.name == name and item.acc_num == acc_num:
                return item

class Card:
    def __init__(self, name, deposit):
        self.name = name
        self.balance = int(deposit)

    def gettingAnAccNum(self,l_com):
        self.acc_num = ""
        for i in range(5):
            n = random.choice(l_com)
            self.acc_num += n
        return self.acc_num

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print(f'This is your card balance: {self.balance}') 


if __name__ == "__main__":
    random.shuffle(l_com)
    bank = Bank()

    while True:
        print('\nPlease choose an option: \n\t1.Create a new card\n\t2.Using an existing account\n\t3.Quit the bank application\n')
        choice = input()
        if choice == "1":
            print('You choose to open a bank account!!')
            name = input('Enter your name:\n\t')
            deposit = input('How much do you want to put into your bank account:\n\t')
            card = Card(name.strip(), deposit)
            bank.addCards(card)
            acc_num = card.gettingAnAccNum(l_com)
            print(f'This is your bank account number: {acc_num}')
        elif choice == "2":
            print("Please enter your name and your account number!")
            name = input('Enter your name:\n\t')
            acc_num = input('Enter your account number:\n\t')
            cus_card = bank.checkExistingCard(bank.cards, name.strip(), acc_num.strip())
            if cus_card != None:
                print('Yes we found your card')
                while True:
                    print('\nChoose an option: \n\t1. Withdraw the money\n\t2. Deposit the money\n\t3. Display the card\n\n\t')
                    choice = input()
                    if choice == "1":
                        amount = int(input('Enter the money you want to withdraw: \n\t'))
                        cus_card.withdraw(amount)
                        cus_card.display()
                        break
                    elif choice == '2':
                        amount = int(input('Enter the money you want to deposit: \n\t'))
                        cus_card.deposit(amount)
                        cus_card.display()
                        break
                    elif choice == '3':
                        cus_card.display()
                        break
            else:
                print("We dont find your card in our system!")
        elif choice == '3':
            print('Thanks for using our product!')
            break
        else:
            print('Please enter from number 1-3')
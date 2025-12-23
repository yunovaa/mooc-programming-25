# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, name, acc_number, balance):
        self.__name = name
        self.__acc_number = acc_number
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount>0:
            self.__balance = amount

    def withdraw(self, amount: float):
        self.__balance-=amount
        self.__service_charge()

    def deposit(self, amount: float):
        self.__balance+=amount
        self.__service_charge()

    def __service_charge(self):
        self.balance-= self.balance*0.01

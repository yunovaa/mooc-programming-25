# TEE RATKAISUSI TÄHÄN:
import math

class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"
    
    def __calc__(self):
        return 100*self.__euros + self.__cents

    def __eq__(self, another: 'Money'):
        return self.__calc__() == another.__calc__()
    
    def __ne__(self, another: 'Money'):
        return self.__calc__() != another.__calc__()
    
    def __gt__(self, another: 'Money'):
        return self.__calc__() > another.__calc__()
    
    def __lt__(self, another: 'Money'):
        return self.__calc__() < another.__calc__()
    
    def __add__(self, another: 'Money'):
        number = self.__calc__() + another.__calc__()
        return Money(number//100, number-number//100*100)
    
    def __sub__(self, another: 'Money'):
        number = self.__calc__() - another.__calc__()
        if number < 0:
            raise ValueError(f"a negative result is not allowed")
        return Money(number//100, number - number//100*100)
    
        

# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, mon, year):
        self.__day = day
        self.__month = mon
        self.__year = year

    def __eq__(self, value: 'SimpleDate'):
        cond = self.__day == value.__day and self.__month ==  value.__month and self.__year == value.__year
        return cond
    
    def __ne__(self, value: 'SimpleDate'):
        return not(self == value)
    
    def __gt__(self, value: 'SimpleDate'):
        if self.__year > value.__year:
            return True
        elif self.__year < value.__year:
            return False
        else:
            if self.__month > value.__month:
                return True
            elif self.__month < value.__month:
                return False
            else:
                if self.__day > value.__day:
                    return True
                else:
                    return False
                
                
    def __lt__(self, value: 'SimpleDate'):
        if self.__year > value.__year:
            return False
        elif self.__year < value.__year:
            return True
        else:
            if self.__month > value.__year:
                return False
            elif self.__month < value.__month:
                return True
            else:
                if self.__day < value.__day:
                    return True
                else:
                    return False
    
    def __add__(self, value):
        
        days, rem = (self.__day + value)%30, (self.__day + value)//30
        months, rem = (self.__month+rem)%12, (self.__month+rem)//12
        years = self.__year + rem
        
        return SimpleDate(days, months, years)

    def __sub__(self, value: 'SimpleDate'):
        return abs((self.__day - value.__day) + (self.__month-value.__month)*30 + (self.__year-value.__year)*360)

    def __str__(self):
        return f'{self.__day}.{self.__month}.{self.__year}'

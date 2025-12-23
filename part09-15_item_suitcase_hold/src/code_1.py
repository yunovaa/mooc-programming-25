# Write your solution here:
class Item:
    def __init__(self, name, kilo):
        self.__name = name
        self.__kilo = kilo

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__kilo
    def __str__(self):
        return f'{self.name()} ({self.weight()} kg)'
    
class Suitcase:
    def __init__(self, max):
        self.__max = max
        self.__item = []

    @property
    def item(self):
        return self.__item

    def weight(self):
        weight = sum([item.weight() for item in self.__item]) 
        return weight
    
    def add_item(self, item: Item):

        if self.weight() + item.weight() <= self.__max:
            self.__item.append(item)

    def heaviest_item(self):
        l = len(self.__item)
        if l==0:
            return None
        mx = max([w.weight() for w in self.__item])
        for item in self.__item:
            if item.weight() == mx:
                return item

    def __str__(self):
        return f'{len(self.__item)} {'item' if len(self.__item)==1 else 'items'} ({self.weight()} kg)'
    
    def print_items(self):
        for i in self.__item:
            print(i)



class CargoHold:
    def __init__(self, max):
        self.__max = max
        self.__item = []

    def weight(self):
        weight = sum([item.weight() for item in self.__item]) 
        return weight   
    
    def add_suitcase(self, item: Suitcase):

        if self.weight() + item.weight() <= self.__max:
            self.__item.append(item)

    def __str__(self):
        return f'{len(self.__item)} {'suitcase' if len(self.__item)==1 else 'suitcases'}, space for {self.__max-self.weight()} kg'
    
    def print_items(self):
        for s in self.__item:
            for item in s.item:
                print(item)


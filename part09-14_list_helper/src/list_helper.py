
# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls, my_list: list):
        d = {my_list.count(number): number  for number in set(my_list)}
        return d[max(d.keys())]
         

    @classmethod
    def doubles(cls, my_list: list):
        return len([number for number in set(my_list) if my_list.count(number)>=2])
    

# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        sur = self.get_sum()
        mex = self.count_numbers()
        return sur/mex if mex != 0 else 0
    
    def odd_sum(self):
        return sum([number for number in self.numbers if number%2])
    
    def even_sum(self):
        return sum([number for number in self.numbers if number%2==0])

def main():
    stats = NumberStats()
    print('Please type in integer numbers: ')

    while True:
        number = int(input())

        if number == -1:
            break

        stats.add_number(number)
    
    print(f'Sum of numbers: {stats.get_sum()}')
    print(f'Mean of numbers: {stats.average()}')
    print(f'Sum of even numbers: {stats.even_sum()}')
    print(f'Sum of odd numbers: {stats.odd_sum()}')

main()

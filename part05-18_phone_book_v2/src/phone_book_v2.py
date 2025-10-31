# Write your solution here
# Write your solution here
phone_book = {}
while True:
    command = int(input('command (1 search, 2 add, 3 quit): '))
    if command == 3:
        print('quitting...')
        break
    name = input('name: ')
    if command == 2:
        number = input('number: ')
        phone_book.setdefault(name, []).append(number)
        print('ok!')
    elif command == 1:
        number_list = phone_book.get(name, [])
        if number_list:
            for number in number_list:
                print(number)
        else:
            print('no number')
    
    

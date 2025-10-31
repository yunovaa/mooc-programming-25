# Write your solution here
def read_file():
    with open('diary.txt') as f:
        return [line.strip() for line in f.readlines()]

def write_file(entry):
    lines = read_file() 
    with open('diary.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
        f.write(entry)
    return None


while True:

    print('1 - add an entry, 2 - read entries, 0 - quit')
    funct = int(input('Function: '))

    if funct == 2:
        print('Entries: ')
        for line in read_file():
            print(line)

    elif funct == 1:
        entry = input('Diary entry: ')
        write_file(entry)
        print('Diary saved')
    
    else:
        break


print('Bye now!')
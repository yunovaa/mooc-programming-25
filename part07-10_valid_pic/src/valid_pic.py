# Write your solution here
import datetime

def is_it_valid(pic: str):

    s = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    date_of_birth = ''
    century_marker = pic[6:7]
    personal_identifier = pic[7:10]
    validate_code = pic[10:]

    if century_marker not in ['+', '-', 'A']:
        print(1)
        return False

    try:

        year = '20'
        if century_marker == '+':
            year = '18'
        elif century_marker == '-':
            year = '19'

        date_of_birth = f'{pic[:4]}{year}{pic[4:6]}'
        print(date_of_birth)
        print(datetime.datetime.strptime(date_of_birth, '%d%m%Y'))

    except:
        print(2)
        return False
    
    index = int(f'{pic[:6]}{personal_identifier}')%31
    
    if validate_code != s[index:index+1]:
        print(3)
        return False
    
    return True


if __name__ == '__main__':
    print(is_it_valid('110986+713J'))
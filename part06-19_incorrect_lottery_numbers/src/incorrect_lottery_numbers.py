# Write your solution here
def filter_incorrect():
    with open('lottery_numbers.csv') as file, open('correct_numbers.csv', 'w') as f:
        l = [(line.split(';')[0].split()[1], (line.split(';')[1].split(','))) for line in file.readlines()]

        for week_number, lot_number in l:
            try:
                
                week_number = int(week_number)

                if len(lot_number) != 7 or len(set(lot_number)) != 7:
                    # print('invalid length')
                    raise ValueError
                
                for number in lot_number:
                    number = int(number)
                    if number<1 or number>39:
                        # print('invalid scope')
                        raise ValueError
                        
                f.write(f'week {week_number};{','.join(lot_number)}')

            except ValueError:
                pass
                # print('not correct')
                

                
if __name__ == '__main__':
    filter_incorrect()
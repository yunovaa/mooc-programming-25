# Write your solution here
import datetime

filename = input('Filename: ')
starting_date = input('Starting date: ')
days = int(input('How many days: '))
print('Please type in screen time in minutes on each day (TV computer mobile):')

starting_date_astime = datetime.datetime.strptime(starting_date, '%d.%m.%Y')
closing_date_astime = starting_date_astime +datetime.timedelta(days=days-1)
l = {}
total = 0

with open(filename, 'w') as file:

    file.write(f'Time period: {datetime.datetime.strftime(starting_date_astime, '%d.%m.%Y')}-{datetime.datetime.strftime(closing_date_astime, '%d.%m.%Y')}\n')
    for i in range(days):
        day = datetime.datetime.strftime(
            starting_date_astime +datetime.timedelta(days=i), '%d.%m.%Y')
        minutes = input(f'Screen time {day}:')

        l[day] = '/'.join(minutes.split())

        total+=sum(map(int, minutes.split()))

    
    file.write(f"Total minutes: {total}\n")
    file.write(f"Average minutes: {total/days}\n")

    for key in l.keys():
        file.write(f'{key}: {l[key]}\n')

    file.close()



# Write your solution here
import datetime

eve_day = datetime.datetime(1999, 12, 31)

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

your_birth = datetime.datetime(year=year, month=month, day=day)

if year>=2000:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f'You were {(eve_day-your_birth).days} days old on the eve of the new millennium.')
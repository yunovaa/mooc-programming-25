# Write your solution here
import csv
import datetime as dt
def cheaters():
    l = []
    with open('start_times.csv') as start_time_file:
        names = {line[0]: dt.datetime.strptime(line[1], "%H:%M")
                 for line in csv.reader(start_time_file, delimiter=';')}
        
    with open('submissions.csv') as sub_file:
        for name in csv.reader(sub_file, delimiter=';'):
            if name[0] not in l:
                sub_time = dt.datetime.strptime(name[-1], "%H:%M")
                start_time = names[name[0]]
                if (sub_time-start_time).seconds>3*60*60:
                    l.append(name[0])
    return l
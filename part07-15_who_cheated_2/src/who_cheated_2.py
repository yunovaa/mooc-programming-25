# Write your solution here
import csv
import datetime as dt
def check_submission(ad, saat):
    with open('start_times.csv') as start_time_file:
        names = {line[0]: dt.datetime.strptime(line[1], "%H:%M")
                 for line in csv.reader(start_time_file, delimiter=';')}
        
    
    
    start_time = names[ad]
    sub_time = dt.datetime.strptime(saat, "%H:%M")
    if (sub_time-start_time).seconds>3*60*60:
        return False
    return True
            


def final_points():
    d = {}
    with open('submissions.csv') as sub_file:
        for line in csv.reader(sub_file, delimiter=';'):
            name = line[0]
            not_cheater = check_submission(name, line[-1])
            if not_cheater:
                if name not in d:
                    d[name] = {}

                ex_number = line[1]
                ex_point = line[2]
                try:
                    ex_point = max(ex_point, d[name][ex_number])
                except KeyError:
                    pass
                finally:
                    d[name][ex_number] = ex_point


    return {key: sum(map(lambda x: int(x), value.values())) for key, value in d.items()}
                
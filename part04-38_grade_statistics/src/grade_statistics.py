# Write your solution here
d = {5: '', 4: '', 3: '', 2: '', 1: '', 0: ''}
gp = 0
c = 0

def stats(ep, xp):
    a = ep
    global gp
        
    if xp == 100:
        a=a+10
    elif xp>=90:
        a+=9
    elif xp>=80:
        a+=8
    elif xp>=70:
        a+=7
    elif xp>=60:
        a+=6
    elif xp>=50:
        a+=5
    elif xp>=40:
        a+=4
    elif xp>=30:
        a+=3
    elif xp>=20:
        a+=2
    elif xp>=10:
        a+=1
    
    if ep<10:
        d[0]+= '*'
    elif a<=14:
        d[0]+='*'
    elif a<=17:
        d[1]+='*'
    elif a<=20:
        d[2]+='*'
    elif a<=23:
        d[3]+='*'
    elif a<=27:
        d[4]+='*'
    elif a<=30:
        d[5]+='*'

    gp+=a


while True:
    points = input('Exam points and exercises completed: ')
    if not points:
        print('Statistics:')
        print(f'Points average: {gp/c:.1f}')
        print(f'Pass percentage: {100*(c-len(d[0]))/c:.1f}')
        print('Grade distribution: ')
        for k, v in d.items():
            print(f' {k}: {v}')
        break
    exam_point = int(points.split()[0])
    exer_point = int(points.split()[1])
    c+=1
    stats(exam_point, exer_point)



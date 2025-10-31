# Write your solution here
l = []
n = 1
while True:
    print(f'The list is now {l}')
    operation = input('a(d)d, (r)emove or e(x)it: ')
    if operation == 'd':
        l.append(n)
        n+=1
    elif operation == 'r':
        l.pop()
        n-=1
    elif operation == 'x':
        print('Bye!')
        break
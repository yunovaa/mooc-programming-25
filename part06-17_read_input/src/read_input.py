# Write your solution here

def read_input(a, b, c):
    while True:
        d = input(a)
        try:
            if b<=int(d) and c>=int(d):
                return int(d)
        except:
            pass

        print(f'You must type in an integer between {b} and {c}')



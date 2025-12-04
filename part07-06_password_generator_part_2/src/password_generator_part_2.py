# Write your solution here
from string import ascii_lowercase
import random
def generate_strong_password(n, bool1, bool2):
    p = '!?=+-()#'
    num = '1234567890'
    s = ''
    passw = ''
    ch1 = random.choice(range(n))
    ch2 = n+1
    ch3 = n+1
    if bool1:
        s+=num
        ch2 = random.choice([a for a in range(n) if a!= ch1])
    if bool2:
        s+=p
        ch3 = random.choice([a for a in range(n) if a!= ch2 and a!=ch1])
    s+=ascii_lowercase

    for i in range(n):
            print(ch1, ch2, ch3)
            if i == ch1:
                passw+= random.choice(ascii_lowercase)

            elif bool1 and i == ch2:
                passw+= random.choice(num)

            elif bool2 and i==ch3:
                passw += random.choice(p)
            else:
                passw += random.choice(s)
    return passw


# for i in range(10):
#     print(generate_strong_password(5, True, True))
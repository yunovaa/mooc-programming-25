# Write your solution here
import random
def generate_password(n):
    s = ''
    return ''.join(chr(random.randint(97, 122)) for i in range(n))
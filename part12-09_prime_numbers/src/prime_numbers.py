# Write your solution here
def prime_numbers():
    number=2
    while True:
        if is_prime(number):
            yield number
        number+=1


def is_prime(number):
    half = number//2
    if number == 2 or number ==3:
        return True
    for i in range(2, half+1):
        if number%i==0:
            return False
    return True
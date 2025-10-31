# Write your solution here
number  = int(input('Please type in a positive integer: '))
neg_number = -1*number
for i in range(number):
    print(neg_number)
    neg_number+=1

for i in range(1, number+1):
    print(i)
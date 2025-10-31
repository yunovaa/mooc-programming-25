# Write your solution here


l = [1, 2, 3, 4, 5]
while True:
    index = int(input('Index: '))
    if index == -1:
        break
    number = int(input('New value: '))
    l[index] = number
    print(l)
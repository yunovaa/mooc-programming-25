# Write your solution here

def filter_solutions():

    with open('correct.csv', 'w') as file:
        file.close()

    with open('incorrect.csv', 'w') as file_n:
        file_n.close()

    with open('solutions.csv') as f:

        for line in f.readlines():
            lists = line.split(';')
            result = int(lists[2])
            check = False
            print(lists[1])
            if '+' in lists[1]:
                a = int(lists[1].split('+')[0])
                b = int(lists[1].split('+')[1])
                
                if a+b == result:
                    check = True

            if '-' in lists[1]:
                a = int(lists[1].split('-')[0])
                b = int(lists[1].split('-')[1])
                
                if a-b == result:
                    check = True

            if check:
                with open('correct.csv', 'a') as file:
                    file.write(line)
            else:
                with open('incorrect.csv', 'a') as file_n:
                    file_n.write(line)


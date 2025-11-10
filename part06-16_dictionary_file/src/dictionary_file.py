# Write your solution here
while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    op = int(input('Function: '))
    if op == 3:
        print('Bye!')
        break
    else:
        with open('dictionary.txt') as file, open('dictionary.txt', 'a') as f:
            words = [(word.split(';')[1], word.split(';')[0]) 
                     for word in file.readlines() if word]

            if op == 2:
                search_term = input('Search term: ')
                for word in words:
                    eng, finn = word
                    if search_term in eng or search_term in finn:
                        print(f'{finn.strip()} - {eng.strip()}')
            
            if op == 1:
                finn = input('The word in Finnish: ')
                eng = input('The word in English: ')
                f.write(f'{finn};{eng}\n')
                print('Dictionary entry added')

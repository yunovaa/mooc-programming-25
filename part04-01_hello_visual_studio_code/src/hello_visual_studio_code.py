# Write your solution here


while True:
    editor = input('Editor: ').title()
    if editor == 'Visual Studio Code':
        print('an excellent choice!')
        break
    elif editor in ['Word', 'Notepad']:
        print('awful')
    else:
        print('not good')

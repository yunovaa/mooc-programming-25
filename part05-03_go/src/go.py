# Write your solution here

def who_won(game_board: list):
    first = 0
    second = 0
    for item in game_board:
        for i in item:
            if i == 1:
                first+=1
            elif i == 2:
                second+=1
    
    if first>second:
        return 1
    elif first<second:
        return 2
    else:
        return 0

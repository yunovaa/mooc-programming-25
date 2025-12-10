# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    
    av1 = person1['result1'] + person1['result2'] + person1['result3']
    av2 = person2['result1'] + person2['result2'] + person2['result3']
    av3 = person3['result1'] + person3['result2'] + person3['result3']

    if av1<av2 and av1<av3:
        return person1
    elif av2<av1 and av2<av3:
        return person2
    else:
        return person3


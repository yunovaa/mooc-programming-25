# Write your solution here

def myFunc(e):
  return len(e)

def shortest(l):
    l.sort(key=myFunc, reverse = True)
    return l[-1]

if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)

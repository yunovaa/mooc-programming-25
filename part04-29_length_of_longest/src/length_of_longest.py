# Write your solution here
def myFunc(e):
  return len(e)

def length_of_longest(l):
    l.sort(key=myFunc)
    return len(l[-1])

if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)

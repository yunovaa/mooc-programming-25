# Write your solution here

def all_the_longest(l):
    a = list(map(len, l))
    return [x for x in l if len(x) == max(a)]

if __name__ == '__main__':
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)
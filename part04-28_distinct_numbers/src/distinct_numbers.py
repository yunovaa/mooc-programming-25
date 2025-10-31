# Write your solution here
def distinct_numbers(l):
    return sorted(list(set(l)))

if __name__ == '__main__' :
    my_list = [1, 10, 1, 100, 1, 1000]
    print(distinct_numbers(my_list)) # [1, 2, 3]
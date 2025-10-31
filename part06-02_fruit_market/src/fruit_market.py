# write your solution here
def read_fruits():
    with open('fruits.csv') as f:
        fruits =  {line.split(';')[0]: float(line.split(';')[1]) for line in f.readlines()}
    return dict(fruits)


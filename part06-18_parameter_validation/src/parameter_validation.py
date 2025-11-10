# Write your solution here
def new_person(name: str, age: int):
    if age<0 or age>150 or name == '' or len(name)>40 or not(' ' in name):
        raise ValueError
    return (name, age)
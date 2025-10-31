# Write your solution here

def oldest_person(people: list):
    year = [year[1] for year in people]
    ind = year.index(min(year))
    return people[ind][0]


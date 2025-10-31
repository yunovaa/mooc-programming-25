# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):

    dict = {
        'name': name,
        'director': director,
        'year': year,
        'runtime': runtime,
    }
    return database.append(dict)


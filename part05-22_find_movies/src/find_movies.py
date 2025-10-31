# Write your solution here
def find_movies(database: list, search_term: str):
    return [movie for movie in database
            if search_term.upper() in movie['name'].upper()]


# Write your solution here:
class Series:

    def __init__(self, title: str, season: int, genre: list):
        self.title = title
        self.season = season
        self.genre = genre
        self.ratings = 0
        self.star = 0

    def __str__(self):
        str = f'{self.title} ({self.season} seasons)\ngenres: {', '.join(self.genre)}\n'
        if self.ratings==0:
            str+= f'no ratings'
        else:
            str+= f'{self.ratings} ratings, average {self.star/self.ratings:.1f} points'
        return str

    def rate(self, rating: int):
        self.ratings+=1
        self.star+=rating

def minimum_grade(rating: float, series_list: list):
    return [series for series in series_list if series.star/series.ratings>=rating]

def includes_genre(genre: str, series_list: list):
    return [series for series in series_list if genre in series.genre]


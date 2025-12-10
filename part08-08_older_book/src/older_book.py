# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------

def older_book(book1: Book, book2: Book):
    case = 1
    if book2.year< book1.year:
        older = book2
    elif book2.year>book1.year:
        older = book1
    else:
        case = 2

    print(f'{book1.name} and {book2.name} were published in {book1.year}' if case==2 else 
          f'{older.name} is older, it was published in {older.year}')
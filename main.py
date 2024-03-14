class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}"

    def __eq__(self, other):
        if isinstance(other, Book):
            return (self.title == other.title) and (self.author == other.author) and (self.genre == other.genre)
        return False


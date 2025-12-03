class Book:
    def __init__(self, author, title, book_id):
        self.author = author
        self.title = title
        self.book_id = book_id

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                break


book1 = Book("Толстой", "Война и мир", 1)
book2 = Book("Достоевский", "Идиот", 2)

library = Library("Городская библиотека")

library.add_book(book1)
library.add_book(book2)

print(library.books)

library.remove_book(1)

print(library.books)

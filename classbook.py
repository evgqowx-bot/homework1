class Book:
    def __init__(self, author: str, title: str, book_id: int):
        self.author = author
        self.title = title
        self.book_id = book_id

    def __str__(self):
        return f"Book(id={self.book_id}, '{self.title}', {self.author})"

    def __repr__(self):
        return f"Book(author={self.author!r}, title={self.title!r}, book_id={self.book_id})"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book_id: int):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                break

    def __str__(self):
        return f"Library '{self.name}' ({len(self.books)} книг)"

    def __repr__(self):
        return f"Library(name={self.name!r}, books={self.books!r})"

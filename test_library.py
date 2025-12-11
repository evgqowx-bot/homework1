import pytest
from classbook import Book, Library

@pytest.fixture
def book1():
    return Book("Толстой", "Война и мир", 1)

@pytest.fixture
def book2():
    return Book("Достоевский", "Идиот", 2)

@pytest.fixture
def library(book1, book2):
    lib = Library("Городская библиотека")
    lib.add_book(book1)
    lib.add_book(book2)
    return lib

class TestBook:
    def test_book_attributes(self, book1):
        assert book1.author == "Толстой"
        assert book1.title == "Война и мир"
        assert book1.book_id == 1

    def test_book_str(self, book1):
        assert str(book1) == "Book(id=1, 'Война и мир', Толстой)"

    def test_book_repr(self, book1):
        assert repr(book1) == "Book(author='Толстой', title='Война и мир', book_id=1)"

class TestLibrary:
    def test_add_book(self, library, book1):
        assert book1 in library.books
        assert len(library.books) == 2

    def test_remove_book(self, library):
        library.remove_book(1)
        assert all(book.book_id != 1 for book in library.books)
        assert len(library.books) == 1

    def test_library_str(self, library):
        assert str(library) == "Library 'Городская библиотека' (2 книг)"

    def test_library_repr(self, library):
        repr_str = repr(library)
        assert "Library(name='Городская библиотека', books=" in repr_str

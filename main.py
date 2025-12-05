from models import Book, Library

book1 = Book("Толстой", "Война и мир", 1)
book2 = Book("Достоевский", "Идиот", 2)

library = Library("Городская библиотека")

library.add_book(book1)
library.add_book(book2)

print(library)
print(library.books)  #

library.remove_book(1)

print(library)
print(library.books)

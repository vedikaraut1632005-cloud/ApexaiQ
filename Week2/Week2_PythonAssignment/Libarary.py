"""This program creates classes for Book, Member, and Library.
Members can borrow or return books, and the Library tracks available and borrowed books."""

class Book:
    """Represents a single book in the library."""

    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    """Represents a library member who can borrow and return books."""

    def __init__(self, name):
        """Initialize a member with their name and an empty list of borrowed books."""
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """Borrow a book if it is available."""
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"'{book.title}' is already borrowed by someone else.")

    def return_book(self, book):
        """Return a borrowed book to the library."""
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} cannot return '{book.title}' (not borrowed).")


class Library:
    """Represents the library that manages books and tracks availability."""

    def __init__(self):
        """Initialize the library with an empty book collection."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self.books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def show_available_books(self):
        """Display all books that are currently available."""
        print("\nAvailable books:")
        for book in self.books:
            if not book.is_borrowed:
                print(f"- {book.title} by {book.author}")
        print()

    def show_borrowed_books(self):
        """Display all books that are currently borrowed."""
        print("\nBorrowed books:")
        for book in self.books:
            if book.is_borrowed:
                print(f"- {book.title} by {book.author}")
        print()




library = Library()


book1 = Book("Python Programming", "John Doe")
book2 = Book("Data Structures", "Jane Smith")
book3 = Book("OOP Concepts", "Alan Turing")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

member1 = Member("Vedika")
member2 = Member("Rahul")


library.show_available_books()


member1.borrow_book(book1)
member2.borrow_book(book2)


library.show_available_books()
library.show_borrowed_books()


member1.return_book(book1)


library.show_available_books()
library.show_borrowed_books()

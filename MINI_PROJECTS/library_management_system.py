"""
====================================================
           LIBRARY MANAGEMENT SYSTEM
====================================================

Concepts:

    OOP
    Classes
    Objects
    Lists
    Methods
    Conditions
"""


class Book:

    def __init__(self, title, author):

        self.title = title

        self.author = author

        self.is_available = True


    def display(self):

        status = (
            "Available"
            if self.is_available
            else "Issued"
        )


        print(
            self.title,
            "-",
            self.author,
            "-",
            status
        )


class Library:

    def __init__(self):

        self.books = []


    def add_book(self, book):

        self.books.append(book)


    def show_books(self):

        for book in self.books:

            book.display()


    def issue_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.is_available:

                    book.is_available = False

                    print("Book issued.")

                else:

                    print("Book already issued.")

                return


        print("Book not found.")


    def return_book(self, title):

        for book in self.books:

            if book.title.lower() == title.lower():

                book.is_available = True

                print("Book returned.")

                return


        print("Book not found.")


# ==================================================
# CREATE LIBRARY
# ==================================================

library = Library()


# Add books

library.add_book(
    Book(
        "Python Programming",
        "Guido van Rossum"
    )
)


library.add_book(
    Book(
        "Clean Code",
        "Robert Martin"
    )
)


# Display books

library.show_books()


# Issue book

library.issue_book(
    "Python Programming"
)


# Display again

library.show_books()


# Return book

library.return_book(
    "Python Programming"
)


library.show_books()
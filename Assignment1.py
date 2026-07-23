class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

class User:
    def __init__(self, name):
        self.name = name
        self.books = []

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, title):
        self.books.append(Book(title))

    def register_user(self, name):
        self.users.append(User(name))

    def borrow_book(self, user_name, book_title):
        for user in self.users:
            if user.name == user_name:
                for book in self.books:
                    if book.title == book_title and book.available:
                        book.available = False
                        user.books.append(book.title)
                        print(user_name, "borrowed", book_title)
                        return
        print("Book not available")

    def return_book(self, user_name, book_title):
        for user in self.users:
            if user.name == user_name and book_title in user.books:
                user.books.remove(book_title)
                for book in self.books:
                    if book.title == book_title:
                        book.available = True
                print(user_name, "returned", book_title)
                return
        print("Return failed")

    def show_books(self):
        for book in self.books:
            if book.available:
                print(book.title, "- Available")
            else:
                print(book.title, "- Borrowed")


library = Library()
library.add_book("Python")
library.add_book("Java")
library.show_books()
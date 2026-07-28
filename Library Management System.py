from datetime import datetime, timedelta

# --------------------- Book Class ---------------------

class Book:
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.available = True

    def display(self):
        status = "Available" if self.available else "Borrowed"
        print(f"""
Book ID   : {self.book_id}
Title     : {self.title}
Author    : {self.author}
Category  : {self.category}
Status    : {status}
""")

# --------------------- Person Class ---------------------

class Person:
    def __init__(self, person_id, name):
        self.person_id = person_id
        self.name = name

# --------------------- Patron Class ---------------------

class Patron(Person):
    def __init__(self, person_id, name):
        super().__init__(person_id, name)
        self.borrowed_books = {}
        self.history = []

# --------------------- Library Class ---------------------

class Library:

    FINE_PER_DAY = 10

    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add Book
    def add_book(self):
        book_id = input("Book ID: ")

        if book_id in self.books:
            print("Book ID already exists!")
            return

        title = input("Title: ")
        author = input("Author: ")
        category = input("Category: ")

        self.books[book_id] = Book(book_id, title, author, category)
        print("Book added successfully.")

    # Register Patron
    def register_patron(self):
        pid = input("Patron ID: ")

        if pid in self.patrons:
            print("Patron already registered.")
            return

        name = input("Name: ")

        self.patrons[pid] = Patron(pid, name)
        print("Patron registered successfully.")

    # View Books
    def view_books(self):

        if not self.books:
            print("No books available.")
            return

        print("\n========== BOOK LIST ==========\n")

        for book in self.books.values():
            book.display()

    # Search Book
    def search_book(self):

        keyword = input("Enter title or author: ").lower()

        found = False

        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                book.display()
                found = True

        if not found:
            print("No matching book found.")

    # Borrow Book
    def borrow_book(self):

        pid = input("Patron ID: ")
        bid = input("Book ID: ")

        if pid not in self.patrons:
            print("Patron not found.")
            return

        if bid not in self.books:
            print("Book not found.")
            return

        book = self.books[bid]
        patron = self.patrons[pid]

        if not book.available:
            print("Book is already borrowed.")
            return

        borrow_date = datetime.now()
        due_date = borrow_date + timedelta(days=14)

        patron.borrowed_books[bid] = due_date
        patron.history.append(f"Borrowed '{book.title}' on {borrow_date.strftime('%d-%m-%Y')}")

        book.available = False

        print("Book borrowed successfully.")
        print("Due Date:", due_date.strftime("%d-%m-%Y"))

    # Return Book
    def return_book(self):

        pid = input("Patron ID: ")
        bid = input("Book ID: ")

        if pid not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[pid]

        if bid not in patron.borrowed_books:
            print("This patron didn't borrow this book.")
            return

        due_date = patron.borrowed_books[bid]
        today = datetime.now()

        fine = 0

        if today > due_date:
            days = (today - due_date).days
            fine = days * self.FINE_PER_DAY

        del patron.borrowed_books[bid]

        patron.history.append(f"Returned '{self.books[bid].title}' on {today.strftime('%d-%m-%Y')}")

        self.books[bid].available = True

        print("Book returned successfully.")

        if fine > 0:
            print("Late Fine: ₹", fine)
        else:
            print("No Fine.")

    # View Patron Details
    def patron_details(self):

        pid = input("Enter Patron ID: ")

        if pid not in self.patrons:
            print("Patron not found.")
            return

        patron = self.patrons[pid]

        print("\n========== PATRON DETAILS ==========")
        print("Name:", patron.name)
        print("Patron ID:", patron.person_id)

        print("\nBorrowed Books:")

        if patron.borrowed_books:
            for bid, due in patron.borrowed_books.items():
                print(self.books[bid].title, "| Due:", due.strftime("%d-%m-%Y"))
        else:
            print("None")

        print("\nHistory:")

        if patron.history:
            for item in patron.history:
                print("-", item)
        else:
            print("No History.")

# --------------------- Main Program ---------------------

library = Library()

while True:

    print("""
==============================
 LIBRARY MANAGEMENT SYSTEM
==============================

1. Add Book
2. Register Patron
3. View Books
4. Search Book
5. Borrow Book
6. Return Book
7. Patron Details
8. Exit

""")

    choice = input("Enter Choice: ")

    try:

        if choice == "1":
            library.add_book()

        elif choice == "2":
            library.register_patron()

        elif choice == "3":
            library.view_books()

        elif choice == "4":
            library.search_book()

        elif choice == "5":
            library.borrow_book()

        elif choice == "6":
            library.return_book()

        elif choice == "7":
            library.patron_details()

        elif choice == "8":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid Choice!")

    except Exception as e:
        print("Error:", e)
 
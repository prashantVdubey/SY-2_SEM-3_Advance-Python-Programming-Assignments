# ---------------- DECORATOR ----------------

def login_required(func):
    def wrapper(user):
        if user.logged_in:
            return func(user)
        else:
            print("\nAccess Denied!")
            print("Please login first.\n")
    return wrapper


# ---------------- USER CLASS ----------------

class User:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.logged_in = False

    # Signup
    def signup(self):

        if self.username != "":
            print("\nAn account already exists!\n")
            return

        print("\n========== SIGN UP ==========")

        self.username = input("Create Username : ")
        self.password = input("Create Password : ")

        print("\nAccount Created Successfully!\n")

    # Login
    def login(self):

        if self.username == "":
            print("\nNo account found. Please Sign Up first.\n")
            return

        print("\n========== LOGIN ==========")

        username = input("Enter Username : ")
        password = input("Enter Password : ")

        if username == self.username and password == self.password:

            self.logged_in = True
            print("\nLogin Successful!\n")

        else:
            print("\nInvalid Username or Password!\n")

    # Logout
    def logout(self):

        if self.logged_in:

            self.logged_in = False
            print("\nLogged Out Successfully!\n")

        else:
            print("\nYou are not logged in.\n")


# ---------------- PROTECTED FUNCTION ----------------

@login_required
def view_dashboard(user):

    print("\n========== DASHBOARD ==========")
    print("Welcome,", user.username)
    print("You have successfully accessed the protected dashboard.")
    print("================================\n")


# ---------------- MAIN PROGRAM ----------------

user = User()

while True:

    print("========== LOGIN AUTHENTICATION SYSTEM ==========")
    print("1. Sign Up")
    print("2. Login")
    print("3. View Dashboard")
    print("4. Logout")
    print("5. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        user.signup()

    elif choice == "2":
        user.login()

    elif choice == "3":
        view_dashboard(user)

    elif choice == "4":
        user.logout()

    elif choice == "5":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")
        
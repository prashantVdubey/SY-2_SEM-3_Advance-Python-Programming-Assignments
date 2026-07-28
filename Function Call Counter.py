# ---------------- DECORATOR ----------------

call_count = {}

def count_calls(func):

    def wrapper(*args, **kwargs):

        if func.__name__ not in call_count:
            call_count[func.__name__] = 0

        call_count[func.__name__] += 1

        print(f"\n{func.__name__} has been called {call_count[func.__name__]} time(s).\n")

        return func(*args, **kwargs)

    return wrapper


# ---------------- FUNCTIONS ----------------

@count_calls
def greet():

    name = input("Enter Your Name : ")
    print("Welcome,", name)


@count_calls
def square():

    num = int(input("Enter Number : "))
    print("Square =", num * num)


# ---------------- MAIN PROGRAM ----------------

while True:

    print("\n===== FUNCTION CALL COUNTER =====")
    print("1. Greeting")
    print("2. Find Square")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        greet()

    elif choice == "2":
        square()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        
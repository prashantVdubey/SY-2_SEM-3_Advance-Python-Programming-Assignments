# ---------------- DECORATOR ----------------

def validate_positive(func):

    def wrapper(*args):

        for value in args:

            if not isinstance(value, int) or value <= 0:
                print("\nError: All arguments must be positive integers.\n")
                return

        return func(*args)

    return wrapper


# ---------------- FUNCTIONS ----------------

@validate_positive
def add_numbers(a, b):
    print("Addition =", a + b)


@validate_positive
def multiply_numbers(a, b):
    print("Multiplication =", a * b)


# ---------------- MAIN PROGRAM ----------------

while True:

    print("\n===== INPUT VALIDATION =====")
    print("1. Add Numbers")
    print("2. Multiply Numbers")
    print("3. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":

        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))

        add_numbers(num1, num2)

    elif choice == "2":

        num1 = int(input("Enter First Number : "))
        num2 = int(input("Enter Second Number : "))

        multiply_numbers(num1, num2)

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
        
from datetime import datetime
import time

# ---------------- DECORATOR ----------------

log_history = []

def function_logger(func):

    def wrapper(*args, **kwargs):

        start_time = time.time()

        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        print("\n========== FUNCTION LOGGER ==========")
        print("Function Name :", func.__name__)
        print("Called At     :", current_time)

        log_history.append(f"{func.__name__} -> {current_time}")

        result = func(*args, **kwargs)

        end_time = time.time()

        print("Execution Time:", round(end_time - start_time, 4), "seconds")
        print("=====================================\n")

        return result

    return wrapper


# ---------------- FUNCTIONS ----------------

@function_logger
def student_report():

    name = input("Enter Student Name : ")
    marks = input("Enter Marks : ")

    print("\n----- Student Report -----")
    print("Name  :", name)
    print("Marks :", marks)


@function_logger
def calculate_sum():

    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))

    print("Sum =", num1 + num2)


# ---------------- DISPLAY LOG ----------------

def show_logs():

    if len(log_history) == 0:
        print("\nNo Function Calls Logged.\n")

    else:

        print("\n========== LOG HISTORY ==========")

        for log in log_history:
            print(log)

        print("=================================\n")


# ---------------- MAIN PROGRAM ----------------

while True:

    print("========== FUNCTION CALL LOGGER ==========")
    print("1. Student Report")
    print("2. Calculate Sum")
    print("3. View Log History")
    print("4. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        student_report()

    elif choice == "2":
        calculate_sum()

    elif choice == "3":
        show_logs()

    elif choice == "4":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice!\n")
        
from datetime import datetime

# -------------------- DECORATORS --------------------

def border(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        func(*args, **kwargs)
        print("=" * 50)
    return wrapper


def footer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("\n******** End of Report ********")
    return wrapper


def generated_date(func):
    def wrapper(*args, **kwargs):
        print("Generated On :", datetime.now().strftime("%d-%m-%Y"))
        func(*args, **kwargs)
    return wrapper


# -------------------- REPORT CLASS --------------------

class Report:

    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.date = datetime.now().strftime("%d-%m-%Y")

    # ---------- CLASS METHODS ----------

    @classmethod
    def student_template(cls):

        author = input("Enter Author Name : ")
        name = input("Enter Student Name : ")
        marks = input("Enter Marks : ")
        grade = input("Enter Grade : ")

        content = (
            f"Student Name : {name}\n"
            f"Marks        : {marks}\n"
            f"Grade        : {grade}"
        )

        return cls("Student Report", author, content)

    @classmethod
    def employee_template(cls):

        author = input("Enter Author Name : ")
        name = input("Enter Employee Name : ")
        department = input("Enter Department : ")
        salary = input("Enter Salary : ")

        content = (
            f"Employee Name : {name}\n"
            f"Department    : {department}\n"
            f"Salary        : {salary}"
        )

        return cls("Employee Report", author, content)

    # ---------- MAGIC METHODS ----------

    def __str__(self):

        return (
            f"Title  : {self.title}\n"
            f"Author : {self.author}\n"
            f"Date   : {self.date}\n\n"
            f"{self.content}"
        )

    def __len__(self):

        return len(str(self))

    def __add__(self, other):

        new_title = self.title + " & " + other.title
        new_author = self.author + " & " + other.author
        new_content = self.content + "\n\n" + other.content

        return Report(new_title, new_author, new_content)

    def __eq__(self, other):

        return (
            self.title == other.title and
            self.author == other.author and
            self.content == other.content
        )


# -------------------- DISPLAY FUNCTION --------------------

@border
@footer
@generated_date
def display_report(report):
    print(report)


# -------------------- MAIN PROGRAM --------------------

print("========== Dynamic Report Generator ==========")
print("1. Student Report")
print("2. Employee Report")

choice = input("Enter Choice : ")

if choice == "1":
    report1 = Report.student_template()

elif choice == "2":
    report1 = Report.employee_template()

else:
    print("Invalid Choice")
    exit()

print("\nFormatted Report\n")
display_report(report1)

print("\nLength of Report :", len(report1))

print("\nCreate Another Report for Comparison")

if choice == "1":
    report2 = Report.student_template()
else:
    report2 = Report.employee_template()

print("\nAre Both Reports Same?")
print(report1 == report2)

print("\nCombined Report\n")

report3 = report1 + report2
display_report(report3)

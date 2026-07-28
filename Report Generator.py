from datetime import datetime

# ---------------- DECORATORS ----------------

def border(func):
    def wrapper(*args, **kwargs):
        print("*" * 40)
        func(*args, **kwargs)
        print("*" * 40)
    return wrapper

def footer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("\n------ End of Report ------")
    return wrapper

# ---------------- REPORT CLASS ----------------

class Report:

    def __init__(self, title, student_name, marks, grade, author):
        self.title = title
        self.student_name = student_name
        self.marks = marks
        self.grade = grade
        self.author = author
        self.date = datetime.now().strftime("%d-%m-%Y")

    # Class Method
    @classmethod
    def student_template(cls):
        return cls(
            "Student Report",
            "Prashant Dubey",
            95,
            "A",
            "Admin"
        )

    # Magic Method (__str__)
    def __str__(self):
        return (
            f"Title   : {self.title}\n"
            f"Author  : {self.author}\n"
            f"Date    : {self.date}\n\n"
            f"Student Name : {self.student_name}\n"
            f"Marks        : {self.marks}\n"
            f"Grade        : {self.grade}"
        )

    # Magic Method (__len__)
    def __len__(self):
        return len(str(self))

    # Magic Method (__add__)
    def __add__(self, other):
        return str(self) + "\n\n" + str(other)

    # Magic Method (__eq__)
    def __eq__(self, other):
        return self.marks == other.marks

# ---------------- DISPLAY FUNCTION ----------------

@border
@footer
def display_report(report):
    print(report)

# ---------------- MAIN PROGRAM ----------------

report1 = Report.student_template()

display_report(report1)

print("\nLength of Report :", len(report1))

report2 = Report(
    "Student Report",
    "Rahul Sharma",
    90,
    "A",
    "Admin"
)

print("\nAre Reports Equal?", report1 == report2)

print("\nCombined Reports:\n")
print(report1 + report2)

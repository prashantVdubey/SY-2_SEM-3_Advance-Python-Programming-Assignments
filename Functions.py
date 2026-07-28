# 1 Required argument
def student(name, roll):
    student_name = name
    student_roll = roll

    print("Student Name:", student_name)
    print("Roll Number:", student_roll)

student("Ashutosh", 24)

# 2 Variable length
def subject(*sub):
    subject = sub
    
    print("Subject:", subject)

subject("Maths", "Python")

# 3 Keyword
def student(name, roll):
    student_name = name
    student_roll = roll

    print("Student Name:", student_name)
    print("Roll Number:", student_roll)
    
student(roll = 35, name = "Ash")

# 4 Default
def student(name, roll, Class = "SY_2"):
    student_name = name
    student_roll = roll
    student_class = Class
    
    print("Student Name:", student_name)
    print("Roll Number:", student_roll)
    print("Student Class:", student_class)
    
student("Ash", 35)
student("Ash", 35, "SY_3")

# 5 Append in list
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("List after appending elements:", numbers)

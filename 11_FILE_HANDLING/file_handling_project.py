"""
====================================================
          SIMPLE STUDENT RECORD SYSTEM
====================================================

This project stores student information
inside a text file.
"""


FILE_NAME = "students.txt"


# ==================================================
# ADD STUDENT
# ==================================================

def add_student():

    name = input("Enter student name: ")

    roll_no = input("Enter roll number: ")

    marks = input("Enter marks: ")


    with open(FILE_NAME, "a") as file:

        file.write(
            f"{roll_no},{name},{marks}\n"
        )


    print("Student added successfully.")


# ==================================================
# VIEW STUDENTS
# ==================================================

def view_students():

    try:

        with open(FILE_NAME, "r") as file:

            data = file.readlines()


        if len(data) == 0:

            print("No students found.")

            return


        print("\nStudent Records")
        print("----------------")


        for line in data:

            roll_no, name, marks = line.strip().split(",")

            print("Roll No:", roll_no)
            print("Name:", name)
            print("Marks:", marks)

            print("----------------")


    except FileNotFoundError:

        print("No student records found.")


# ==================================================
# MAIN PROGRAM
# ==================================================

while True:

    print("\n===== STUDENT MANAGEMENT =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")


    choice = input("Enter your choice: ")


    if choice == "1":

        add_student()


    elif choice == "2":

        view_students()


    elif choice == "3":

        print("Program ended.")

        break


    else:

        print("Invalid choice.")
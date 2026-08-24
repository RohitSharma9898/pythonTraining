"""
STUDENT REGISTRATION SYSTEM

Uses:
- Functions
- Classes
- Exception Handling
- Custom Exceptions
"""


class InvalidMarksError(Exception):

    pass


class InvalidAgeError(Exception):

    pass


class Student:

    def __init__(self, name, age, marks):

        self.name = name
        self.age = age
        self.marks = marks

    def display(self):

        print("\nStudent Details")

        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


def create_student():

    try:

        name = input("Enter name: ")

        age = int(input("Enter age: "))

        marks = float(input("Enter marks: "))


        # Validate age

        if age <= 0:

            raise InvalidAgeError(
                "Age must be greater than 0"
            )


        # Validate marks

        if marks < 0 or marks > 100:

            raise InvalidMarksError(
                "Marks must be between 0 and 100"
            )


        student = Student(
            name,
            age,
            marks
        )


        student.display()


    except ValueError:

        print("Please enter valid numeric values.")

    except InvalidAgeError as error:

        print("Age Error:", error)

    except InvalidMarksError as error:

        print("Marks Error:", error)


create_student()
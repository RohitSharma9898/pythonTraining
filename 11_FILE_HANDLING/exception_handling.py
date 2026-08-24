"""
FILE HANDLING WITH EXCEPTION HANDLING
"""


try:

    with open("student.txt", "r") as file:

        data = file.read()

        print(data)


except FileNotFoundError:

    print("The file does not exist.")


except PermissionError:

    print("You don't have permission to access this file.")
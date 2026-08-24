"""
FILE POINTER

The file pointer tells us the current
position inside the file.
"""


with open("student.txt", "r") as file:

    print("Initial position:", file.tell())

    data = file.read(5)

    print("Data:", data)

    print("Current position:", file.tell())
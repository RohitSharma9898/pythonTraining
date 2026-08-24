"""
tell()

tell() returns the current position
of the file pointer.
"""


with open("student.txt", "r") as file:

    print("Position:", file.tell())

    file.read(10)

    print("Position:", file.tell())

    file.read(5)

    print("Position:", file.tell())
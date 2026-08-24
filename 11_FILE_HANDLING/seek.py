"""
seek()

seek() moves the file pointer
to a specific position.
"""


with open("student.txt", "r") as file:

    print(file.read(5))


    # Move pointer back to beginning

    file.seek(0)


    print(file.read(5))
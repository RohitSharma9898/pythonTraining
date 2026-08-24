"""
WITH STATEMENT

The with statement automatically closes
the file after the operation is complete.

This is safer and cleaner than manually
calling file.close().
"""


# ==========================================
# WITHOUT with
# ==========================================

file = open("student.txt", "r")

data = file.read()

print(data)

file.close()


# ==========================================
# WITH with
# ==========================================

with open("student.txt", "r") as file:

    data = file.read()

    print(data)


"""
The file is automatically closed
after leaving the with block.
"""
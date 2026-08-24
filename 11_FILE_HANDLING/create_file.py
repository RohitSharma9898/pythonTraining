"""
CREATE A FILE

We can create a file using open().

Mode:
    "w" -> write mode
    "a" -> append mode
    "x" -> create a new file
"""


# ==========================================
# CREATE USING WRITE MODE
# ==========================================

file = open("student.txt", "w")

file.close()


print("File created successfully.")


# ==========================================
# CREATE USING x MODE
# ==========================================

"""
"x" creates a new file.

If the file already exists,
Python will raise FileExistsError.
"""

try:

    file = open("new_student.txt", "x")

    file.close()

    print("New file created.")

except FileExistsError:

    print("File already exists.")
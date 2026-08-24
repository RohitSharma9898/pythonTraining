"""
FILE MODES
"""


# ==========================================
# r -> READ
# ==========================================

with open("student.txt", "r") as file:

    print(file.read())


# ==========================================
# w -> WRITE
# ==========================================

with open("student.txt", "w") as file:

    file.write("Hello Python")


# ==========================================
# a -> APPEND
# ==========================================

with open("student.txt", "a") as file:

    file.write("\nWelcome to Python")


# ==========================================
# x -> CREATE
# ==========================================

try:

    with open("new_file.txt", "x") as file:

        file.write("New file created.")

except FileExistsError:

    print("File already exists.")


"""
Common modes:

r  -> read
w  -> write
a  -> append
x  -> create

Additional:

r+ -> read + write
w+ -> write + read
a+ -> append + read
"""
"""
readlines()

Reads all lines and returns
them as a list.
"""


file = open("student.txt", "r")


lines = file.readlines()


print(lines)


file.close()


# ==========================================
# PRINT EACH LINE
# ==========================================

file = open("student.txt", "r")


lines = file.readlines()


for line in lines:

    print(line.strip())


file.close()
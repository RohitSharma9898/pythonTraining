"""
BREAK STATEMENT

break is used to immediately stop a loop.
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

for i in range(1, 11):

    if i == 5:
        break

    print(i)


# ==========================================
# FIND A NUMBER
# ==========================================

numbers = [10, 20, 30, 40, 50]

for number in numbers:

    if number == 30:
        print("Number found!")
        break

    print("Checking:", number)


# ==========================================
# STOP WHEN USER ENTERS 0
# ==========================================

while True:

    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break

    print("You entered:", number)

print("Loop ended.")


# ==========================================
# BREAK IN NESTED LOOP
# ==========================================

for i in range(1, 4):

    for j in range(1, 4):

        if j == 2:
            break

        print(i, j)
"""
WHILE LOOP

A while loop repeats code as long as
the condition is True.

Syntax:

while condition:
    statement
"""

# ==========================================
# BASIC EXAMPLE
# ==========================================

i = 1

while i <= 5:
    print(i)
    i = i + 1


# ==========================================
# PRINT 1 TO 10
# ==========================================

i = 1

while i <= 10:
    print(i)
    i += 1


# ==========================================
# EVEN NUMBERS
# ==========================================

i = 2

while i <= 10:
    print(i)
    i += 2


# ==========================================
# USER CONTROLLED LOOP
# ==========================================

number = int(input("Enter a number: "))

while number != 0:

    print("You entered:", number)

    number = int(input("Enter another number (0 to stop): "))


# ==========================================
# COUNTDOWN
# ==========================================

count = 5

while count >= 1:
    print(count)
    count -= 1

print("Go!")


# ==========================================
# IMPORTANT
# ==========================================

# Make sure the condition eventually becomes False.

# Otherwise, the loop can become an infinite loop.

# Example:

# while True:
#     print("This will run forever.")
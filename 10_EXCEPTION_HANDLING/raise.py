"""
RAISE

raise is used to manually create
an exception.
"""


# ==========================================
# AGE VALIDATION
# ==========================================

age = int(input("Enter your age: "))


if age < 18:

    raise ValueError("Age must be 18 or above")


print("You are eligible")


# ==========================================
# MARKS VALIDATION
# ==========================================

def check_marks(marks):

    if marks < 0 or marks > 100:

        raise ValueError("Marks must be between 0 and 100")

    print("Valid marks")


check_marks(90)

# check_marks(150)
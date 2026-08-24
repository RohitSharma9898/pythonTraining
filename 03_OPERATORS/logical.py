"""
LOGICAL OPERATORS

Logical operators are used to combine conditions.

and
or
not
"""

# ==========================================
# AND
# ==========================================

# Returns True only when BOTH conditions are True.

age = 21
has_id = True

print(age >= 18 and has_id)


# One condition False

age = 16
has_id = True

print(age >= 18 and has_id)


# ==========================================
# OR
# ==========================================

# Returns True when AT LEAST ONE condition is True.

has_email = True
has_phone = False

print(has_email or has_phone)


# Both False

has_email = False
has_phone = False

print(has_email or has_phone)


# ==========================================
# NOT
# ==========================================

is_raining = False

print(not is_raining)


is_logged_in = True

print(not is_logged_in)


# ==========================================
# COMBINING OPERATORS
# ==========================================

age = 25
has_id = True
has_ticket = True

result = age >= 18 and has_id and has_ticket

print("Can enter:", result)


# ==========================================
# PRACTICAL EXAMPLE
# ==========================================

username = "admin"
password = "1234"

login = username == "admin" and password == "1234"

print("Login successful:", login)


# ==========================================
# TRUTH TABLE
# ==========================================

print("AND")
print(True and True)
print(True and False)
print(False and True)
print(False and False)


print("\nOR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)


print("\nNOT")
print(not True)
print(not False)
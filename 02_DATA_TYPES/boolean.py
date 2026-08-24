"""
Boolean Data Type

Boolean has only two values:

True
False
"""

# Basic Boolean values

is_student = True
is_teacher = False

print(is_student)
print(is_teacher)

print(type(is_student))


# Boolean using comparison operators

age = 21

print(age >= 18)
print(age < 18)
print(age == 21)
print(age != 21)


# Boolean expressions

x = 10
y = 20

print(x > y)
print(x < y)
print(x == y)


# Boolean with logical operators

age = 21
has_id = True

print(age >= 18 and has_id)

print(age >= 18 or has_id)

print(not has_id)


# bool() function

print(bool(1))
print(bool(0))

print(bool("Hello"))
print(bool(""))

print(bool([1, 2, 3]))
print(bool([]))


# Important concept:
# The following values are generally considered False:

print(bool(0))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))


# Everything else is generally True

print(bool(10))
print(bool(-10))
print(bool("Python"))
print(bool([1, 2]))
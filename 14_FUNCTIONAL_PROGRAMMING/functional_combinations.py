"""
====================================================
          COMBINING FUNCTIONAL TOOLS
====================================================

We can combine:

    map()
    filter()
    lambda()
"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# Step 1:
# Keep only even numbers

even_numbers = filter(
    lambda number: number % 2 == 0,
    numbers
)


# Step 2:
# Square the even numbers

squares = map(
    lambda number: number * number,
    even_numbers
)


print(list(squares))


"""
Flow:

numbers
   ↓
filter()
   ↓
even numbers
   ↓
map()
   ↓
squared numbers
"""
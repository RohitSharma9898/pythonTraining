"""
MEMORY COMPARISON

Generators are useful when working
with large amounts of data.
"""

import sys


# ==========================================
# LIST
# ==========================================

numbers_list = [x for x in range(10000)]


print(
    "List memory:",
    sys.getsizeof(numbers_list),
    "bytes"
)


# ==========================================
# GENERATOR
# ==========================================

numbers_generator = (
    x for x in range(10000)
)


print(
    "Generator memory:",
    sys.getsizeof(numbers_generator),
    "bytes"
)


"""
The list stores all generated values.

The generator produces values when
they are requested.

This is why generators are useful
for large data processing.
"""
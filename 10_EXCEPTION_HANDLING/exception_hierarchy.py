"""
EXCEPTION HIERARCHY

Most built-in exceptions ultimately
inherit from BaseException.

A common structure is:

BaseException
      |
      Exception
      |
      ├── ValueError
      ├── TypeError
      ├── IndexError
      ├── KeyError
      └── ZeroDivisionError
"""


try:

    number = 10 / 0

except Exception as error:

    print("Exception handled:", error)


# ==========================================
# IMPORTANT
# ==========================================

"""
Generally prefer catching specific exceptions.

Better:

except ValueError:

instead of:

except Exception:

because specific exceptions make your
program easier to understand and debug.
"""
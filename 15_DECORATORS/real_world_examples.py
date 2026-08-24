"""
====================================================
             REAL-WORLD DECORATORS
====================================================
"""


# ==================================================
# EXAMPLE 1: LOGIN CHECK
# ==================================================

def login_required(function):


    def wrapper(is_logged_in):

        if not is_logged_in:

            print("Please login first.")

            return


        function(is_logged_in)


    return wrapper


@login_required
def dashboard(is_logged_in):

    print("Welcome to your dashboard!")


dashboard(True)

dashboard(False)


# ==================================================
# EXAMPLE 2: ADMIN CHECK
# ==================================================

def admin_required(function):


    def wrapper(role):

        if role != "admin":

            print("Access denied.")

            return


        function(role)


    return wrapper


@admin_required
def delete_user(role):

    print("User deleted successfully.")


delete_user("admin")

delete_user("student")


# ==================================================
# EXAMPLE 3: LOGGING
# ==================================================

def log_function(function):


    def wrapper(*args, **kwargs):

        print("Function called:", function.__name__)

        result = function(*args, **kwargs)

        print("Function finished.")

        return result


    return wrapper


@log_function
def add(a, b):

    return a + b


print(add(10, 20))
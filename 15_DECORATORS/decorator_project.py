"""
====================================================
          SIMPLE ACCESS CONTROL SYSTEM
====================================================

We will use decorators to control access
to different functions.
"""


# ==================================================
# LOGIN DECORATOR
# ==================================================

def login_required(function):


    def wrapper(user):

        if not user["logged_in"]:

            print("Please login first.")

            return


        return function(user)


    return wrapper


# ==================================================
# ADMIN DECORATOR
# ==================================================

def admin_required(function):


    def wrapper(user):

        if user["role"] != "admin":

            print("You don't have admin permission.")

            return


        return function(user)


    return wrapper


# ==================================================
# USER FUNCTIONS
# ==================================================

@login_required
def profile(user):

    print("Profile opened.")


@login_required
@admin_required
def delete_user(user):

    print("User deleted.")


# ==================================================
# USERS
# ==================================================

admin = {

    "name": "Rohit",

    "logged_in": True,

    "role": "admin"
}


student = {

    "name": "Rahul",

    "logged_in": True,

    "role": "student"
}


guest = {

    "name": "Aman",

    "logged_in": False,

    "role": "student"
}


# ==================================================
# TEST
# ==================================================

print("\nAdmin:")

delete_user(admin)


print("\nStudent:")

delete_user(student)


print("\nGuest:")

delete_user(guest)
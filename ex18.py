# Your function should have a short name, and it should say what it does.
# All lines indented by four spaces after the colon (:) become part of the body of the function.
# Anything that does not start with a number and is letters, numbers, and underscores will work as function name.
def print_two(*args):  # * tells Python to take arguments and make a list args of them.
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# We can do without *args too!
def print_two_again(arg1, arg2):  # No duplicate names as arguments to function.
    print(f"arg1: {arg1}, arg2: {arg2}")


# Function below takes only one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# This function takes no arguments.
def print_none():
    print("I got no arguments!", end=' ')
    print("I got nothing to do!")


print_two("Rana", "Dilshad")
print_two_again("Rana", "Dilshad")
print_one("Dilshad")
print_none()

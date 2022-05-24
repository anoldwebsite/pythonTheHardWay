# while loop
# A while-loop will keep executing the code block under it as long as a Boolean expression is True.
i = 0
numbers = []
while i < 6:
    print("At the top i is", i)
    numbers.append(i ** 2)
    i += 1
    print("Our updated list now:", numbers)
    print(f"At the bottom i is {i}")
    print("£££££££££££££££££££££££")

print(numbers)
print("Elements in the list are:")
for element in numbers:
    print(element)

"""
“To avoid these problems, there are some rules to follow:
1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
2. Review your while statements and make sure that the Boolean test will become False at some point.
3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it’s doing.”

Excerpt From
Learn Python 3 the Hard Way: A Very Simple Introduction to the Terrifyingly Beautiful World of Computers and Code (Zed Shaw's Hard Way Series)
Zed A. Shaw
This material may be protected by copyright.
"""


# “Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.”

def my_func(counter):
    i = 0
    square_list = []
    while i < counter:
        print("i at the top:", i)
        square_list.append(i ** 2)
        i += 1
        print(f"Updated list: {square_list}")
        print("i at the bottom:", i)
        print("€€€€€€€€€€€€€€€€€€€€€€")


my_func(10)


# “Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.”
def my_func2(*my_args):
    # value_if_true if condition else value_if_false
    counter = my_args[0] if (len(my_args) >= 1 and my_args[0] > 0) else 10
    step = my_args[1] if (len(my_args) >= 2 and my_args[1] > 0) else 1

    i = 0
    square_list = []
    while i < counter:
        print("i at the top:", i)
        square_list.append(i ** 2)
        i += step
        print(f"Updated list: {square_list}")
        print("i at the bottom:", i)
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


# The function needs two arguments but the user sends none. Prevent error throwing.
my_func2()
# The function needs two arguments but the user sends one. Prevent error throwing.
# my_func2(20)
# my_func2(20, 5)
# my_func2(20, 5, 12)  # No error will be thrown but we are not using the third argument in our function.

# “Write it to use for-loops and range. Do you need the incrementor in the middle anymore? What happens if you do not get rid of it?”
# def my_func3():

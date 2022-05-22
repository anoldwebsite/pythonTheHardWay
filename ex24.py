print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and required an explanation
\n\t\twhere there is none.
"""

print("-------------------------------")
print(poem)
print("-------------------------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates  # Returning a tuple


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# Remember that this is another way to format strings.
print("With a starting point of : {}".format(start_point))
# It's just like with an f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)  # A tuple is returned by the function.
# This is an easy way to apply a list to a format string.
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))  # * before a tuple or list unpacks a list
# print(type(formula))  # <class 'tuple'>
# print(formula)  # (500000.0, 500.0, 5.0)

"""
>>> numbers = (1, 2, 3)
>>> numbers
(1, 2, 3)
>>> more_numbers = (*numbers, 4, 5)
>>> print(more_numbers)
(1, 2, 3, 4, 5)
"""

"""
>>> numbers = [1, 2, 3, 4]
>>> numbers
[1, 2, 3, 4]
>>> more_numbers = [*numbers, 5, 6]
>>> more_numbers
[1, 2, 3, 4, 5, 6]
>>> print(more_numbers)
[1, 2, 3, 4, 5, 6]
>>> print(*more_numbers)
1 2 3 4 5 6
>>> print(*more_numbers, sep=', ')
1, 2, 3, 4, 5, 6
>>>
"""

"""
>>> def secret_formula(started):
...     jelly = started * 500
...     jars = jelly / 1000
...     crates = jars / 100
...     return jelly, jars, crates
... 
>>> print(type(secret_formula(10000)))
<class 'tuple'>
>>> print(secret_formula(10000))
(5000000, 5000.0, 50.0)
>>> print(*secret_formula(10000))
5000000 5000.0 50.0
>>> print(*secret_formula(10000), sep=', ')
5000000, 5000.0, 50.0
"""
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# Going through the loop above
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print("A fruit of type:", fruit)

for i in change:
    print(f"I got {i}")

# We can even start with an empty list adn then build it.
elements = []
# We can use a range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)  # append is a function that appends an item to anlist.

# Printing our list elements
for i in elements:
    print(f"Element was: {i}")

# Using range function with one argument.
elements.clear()  # Clears the list, and now we have an empty list.
print(f"List elements: {elements}")
for i in range(4):
    elements.append(i)

print(f"List elements: {elements}")

# List of lists. 2-D list
employees = [1, 2,
             ["Rana", "Dilshad", "Qais", "Russell", "Jenny", "Jane"],
             ["Software Architect", "System Developer", "Software Engineer", "Requirement Engineer", "Manager",
              "Sales Manager"],
             ["Production", 'Production', 'Production', "Production", "HR", "Marketing"],
             [55000, 99000.99, 120000, 79000, 123000, 200000],
             4, 5,
             ]
# Printing employees which is a list of lists and other elements.
for i in employees:
    if isinstance(i, list):
        for j in i:
            print(j)
    else:
        print(i)


# Naive and long way to do it: Finding depth of list with recursion
def flat(l):
    depths = []
    for item in l:
        if isinstance(item, list):
            depths.append(flat(item))
    if len(depths) > 0:
        return 1 + max(depths)  # The depth of a list is one more than the maximum depth of its sub-lists.
    return 1


print("Function max")
my_list = ["John doe", "Jane Doe"]
print(max(my_list))
my_list = [-10, 20.12]
print(max(my_list))

some_list = [1, 2, 3, 4, 5, 4, 5, 6]


def cube(some_list2):
    cubes = []
    for num in some_list2:
        cubes.append(num ** 3)
    return cubes


def cube_again(num):
    return num ** 3


print("***********************")
"""
The map() function (which is a built-in function in Python) is used to apply a function 
to each item in an iterable (like a Python list or dictionary). 
It returns a new iterable (a map object) that you can use in other parts of your code.
"""
map_output = map(cube_again, some_list)
print(f"type(map_output): {type(map_output)}")
print(
    f"list(map_output): {list(map_output)}")  # You can make a list of the object of <class 'map'> returned by function map()
print(
    f"set(map_output): {set(map_output)}")  # You can make a list of the object of <class 'map'> returned by function map()
print(
    f"max(map(cube_again, some_list)): {max(map(cube_again, some_list))}")  # You can find max in the map object of <class 'map'> returned by function map()
print(
    f"min(map(cube_again, some_list)): {min(map(cube_again, some_list))}")  # You can find max in the map object of <class 'map'> returned by function map()
print(
    f"sum(map(cube_again, some_list)): {sum(map(cube_again, some_list))}")  # You can find max in the map object of <class 'map'> returned by function map()
print(
    f"set(map(cube_again, some_list)): {set(map(cube_again, some_list))}")  # You can find max in the map object of <class 'map'> returned by function map()
print("***********************")
print(True and max(2, 3, 409))
print(False and max(2, 3, 409))
print(True and max(map(cube_again, some_list)))
print(True and max(map(cube_again, some_list)) + 1)
print("***********************")
print(True and max(map(cube_again, some_list)) + 1 if some_list else 1)
some_list = []
print(True and max(map(cube_again, some_list)) + 1 if some_list else 1)
print("***********************")


# one-liner to find depth of a list
def depth(l):
    return isinstance(l, list) and max(map(depth, l)) + 1 if l else 1  # https://docs.python.org/3.9/library/functions.html#map


print(depth(employees))
print(depth([3, 6, 7, 'happy', [True, None]]))
print(depth([]))
print(flat([]))
print(depth(9))

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now, I'm going to ask you to type three lines.")
line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print(f"I'm writing these lines to the file {filename}.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
target.truncate()

"""
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
"""


print("And finally, we close the file {}.".format(filename))
target.close()

print("*******************************************")
# Read the file from the command line as shown below.
"""
>>> with open("test.txt", 'r') as file1:
...     file_content = file1.read()
...     print(file_content)
... 
This is line one.
This is line two.
This is line three.

>>> 
"""

# Other sample runs to demonstrate readlines() and looping through.
"""
>>> with open("test.txt") as file1:
...     file_content = file1.readlines()
...     print(file_content)
... 
['one\n', 'two\n', 'three\n']
>>> with open("test.txt") as file1:
...     file_content = file1.read()
...     print(file_content)
... 
one
two
three

>>> with open("test.txt") as file1:
...     for line in file1:
...             print(line)
... 
one

two

three

>>>
"""
print("*******************************************")
# Run this file from the command line and pass arguments

from sys import argv

# If the user gives input on the command line, then you use argv
print(argv)  # ['ex13.py', 'apple', 'coffee', 'milk']
print(argv[2])
print("///////////////////////////////////////////////////////")
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# Type this command on the command line: python3 ex13.py 1st 2nd 3rd
# Type this command on the command line: python3 ex13.py apple banana orange
# Type this command on the command line: python3 ex13.py tea coffee milk


"""
You tpe on the command line: python3 ex13.py 1st 2nd 3rd

This should print:
    The script is called: ex13.py
    Your first variable is: 1st
    Your second variable is: 2nd
    Your third variable is: 3rd
"""


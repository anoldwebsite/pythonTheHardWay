# Debug the following program and then run it to make sure that there is no problem left in the code.
# https://learnpythonthehardway.org/python3/exercise26.txt
# Run it from the command line like this: python ex26.py exex1.txt
from sys import argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

script, filename = argv

txt = open(filename)

print("Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())


print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cates = 30
dogs = 15


if people < cates:
    print("Too many cats! The world is doomed!")

if people < cates:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")


if people == dogs:
    print("People are dogs.")

# output when run on terminal after debugging is shown below.

"""
(base) anoldwebsite$ python ex26.py exex1.txt
How old are you? 34
How tall are you? 365
How much do you weigh? 34
So, you're 34 old, 365 tall and 34 heavy.
Here's your file {filename}:
This is line A
This is line B
This is line C
This is line D.

Type the filename again:
> exex1.txt
This is line A
This is line B
This is line C
This is line D.

Let's practice everything.
You'd need to know 'bout escapes with \ that do 
 newlines and 	 tabs.
--------------

	The lovely world
with logic so firmly planted
cannot discern 
 the needs of love
nor comprehend passion from intuition
and requires an explanation

		where there is none.

--------------
This should be five: 5
With a starting point of: 10000
We'd have 5000000 beans, 5000.0 jars, and 50.0 crates.
We can also do that this way:
We'd have 500000.0 beans, 500.0 jars, and 5.0 crates.
Too many cats! The world is doomed!
Not many cats! The world is saved!
The world is dry!
People are greater than or equal to dogs.
People are less than or equal to dogs.
People are dogs.
(base) anoldwebsite$ 

"""

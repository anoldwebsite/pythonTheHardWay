types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

# hilarious is a variable of type boolean, and we assign value False to it.
hilarious = False
special = True
joke_evaluation = "Isn't that joke so funny?! {}. She thinks the opposite. {}"

print(joke_evaluation.format(hilarious, special))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

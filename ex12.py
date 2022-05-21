age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
print("*" * 12)

print("Your eldest child is ", input("How old is your eldest child? "), ".")  # Extra spaces before and after age in output.
print("Your eldest child is", input("How heavy is your eldest child? ") + " kg heavy.")
print("Your eldest child is " + input("How tall is your eldest child? ") + " tall.")

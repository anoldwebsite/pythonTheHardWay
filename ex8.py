
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# Calling the format function of the string formatter
# Pass 4 arguments to format function to match up with the 4 {} in the formatter variable.
print(formatter.format(formatter, formatter, formatter, formatter))
# This will print a new string that has the {} replaced with the 4 {} variables.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

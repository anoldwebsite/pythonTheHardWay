print("I will now count my chickens")
"""
What is the order of opeations?
    PEMDAS
    *****
    Parenthesis
    Exponents
    Multiplication
    Divison
    Addition
    Subtraction
    
    The actual order is you do the multiplication and division in one step,
    from left to right, then you do the addition and subtraction in one step.
    So we can re-write PEMDAS as
    PE(M&D)(A&S)
"""
print("Hens", 25 + 30 / 6) # Hens 30.0 (The comma is not printed.)
print("Roosters", 100 - 25 * 3 % 4)
"""
    100 - 25 == 75
    75 % 4 == 3
    100 - 3 == 97
"""
print("Now, I'l count the eggs.")
print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")
print("How about some more?")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# If you want to be more accurate, use floating points
print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)
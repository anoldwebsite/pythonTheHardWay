my_name = "Dilshad Rana"
my_age = 65
my_height = 74 # inches
my_weight = 125 # kg
my_eyes = "Brown"
my_teeth = "White"
my_hair = "White"

print(f"Let's tal about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"His height in centimeters would be {my_height * 2.54} centimeters.")
print(f"He's {my_weight} kilogram heavy.")
print(f"His weight in pounds would be {my_weight * 2,20462} pounds.")
print(f"Actually that is obese!")
print(f"His BMI is {my_weight / ((my_height * 2.54 )/ 100)}.")  # BMI = kg/m2
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on when he has brushed last.")
# This line is tricky. Try to get it exactly right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight}, I get {total}.")
# \n is for new line
bio = "Name: {}, \n Age: {},\n height: {},\n weight: {},\n Color of eyes: {},\n Color of teeth: {},\n Color of hair: {}"
print(bio.format(my_name, my_age, my_height, my_weight, my_eyes, my_teeth, my_hair))

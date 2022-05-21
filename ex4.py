cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driver = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driver, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")

"""
    _ is called underscore
    = assignment operator is used to assign values to variables which are on the left side of = sign.
    == sign tests for equality
    != sign tests for inequality.
    
    The program uses space_in_a_car = 4.0. What happens if you use space_in_a_car = 4 instead.
    

"""
cars = 100 # cars in the fleet
space_in_a_car = 4.0 # number of passengers that can fit in a car
drivers = 30 # number of drivers
passengers = 90 # number of passengers
cars_not_driven = cars - drivers # extra cars without drivers
cars_driven = drivers # number of cars cars driven
carpool_capacity = cars_driven * space_in_a_car # total number of passengers we can transport
average_passengers_per_car = passengers / cars_driven # avg number of passengers in each car


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")

'''Study Drills
    Python error car_pool_capacity is not defined because on line 7
    it is defined as carpool_capacity all one word for carpool.

    1. If it's 4.0 it's a floating number versus just an integer.
    It's not necessary but preserves flexibility for later

    3. comments added above.

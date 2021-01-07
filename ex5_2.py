# About Zed Shaw in inches and lbs
name = 'Zed A. Shaw'
age = 35 # not a lie
height_in_inches = 74 # inches
weight_in_lbs = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_inches} inches tall.")
print(f"He's {weight_in_lbs} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height_in_inches + weight_in_lbs
print(f"If I add {age}, {height_in_inches}, and {weight_in_lbs} I get {total}.")

inch = 1
cm = 2.54 # inches
height_in_cm = height_in_inches / cm


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

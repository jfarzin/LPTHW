# About Zed Shaw
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# convert height and weight to metric units
inch_to_cm = 2.54
lbs_to_kg = 0.453592
height = height * inch_to_cm
weight = weight * lbs_to_kg

# Update text to reflect metric units
print(f"Let's talk about {name}.")
print(f"He's {round(height)} cm tall.")
print(f"He's {round(weight)} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + round(height) + round(weight)
print(f"If I add {age}, {round(height)}, and {round(weight)} I get {total}.")

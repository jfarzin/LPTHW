age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

age = float(input("How old are you? "))
height = input(f"You're {age}. And how tall are you?")
address = input("What is your address? ")
city = input("What city do you live in? ")
zip_code = int(input(f"What is your zip code in {city}? "))

print(f"Welcome home to {address}, {city}, {zip_code}")


print (f"So, you're {age} old, {height} tall and {weight} heavy.")

# OR 
print (f"So, you're {age} old, {height} tall and", end = ' ')
print (f"{weight} heavy.")

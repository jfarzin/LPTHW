#Take a test, clean up this code to celebrate being almost 
#half-way done with this class

#collect demographic info from user
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")
print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#print(">>demographic data known.")

#open text file and print contents
filename = input("What text file shall we read: ")
txt = open(filename)
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
#print(">>read supplemental file passed from command line.")

#get a new text file and print contents
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()
#print("<<read final file, input from user.")

#print(">>start lesson 24 edits.")
print('Let\'s practice everything.')
print('You\'d need to know \'bout escapes', end = ' ') 
print('with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    """Secret formula for jelly bean distribution within"""
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 10
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
#print("<< completed ex24")

#print(">>final cleanup")
people = 20
cats = 30
dogs = 15
#print(f">> people: {people}, cats: {cats}, dogs: {dogs}")

#print(">>start if statements")
if (people < cats):
    print("Too many cats! The world is doomed!")
    
if (people < cats):
    print("Not many cats! The world is saved!")

if (people < dogs):
    print("The world is drooled on!")

if (people > dogs):
    print("The world is dry!")
#print(">> through first set of if statements")

dogs += 5
#print(f">> people: {people}, cats: {cats}, dogs: {dogs}")

if (people >= dogs):
    print("People are greater than or equal to dogs.")

if (people <= dogs):
    print("People are less than or equal to dogs.")

if (people == dogs):
    print("People are dogs.")

print("<< we passed our test!")
# Define how many types of people there are
types_of_people = 10
# define x, a string that says how many types of people there are
x = f"There are {types_of_people} types of people."

# short-hand for binary and don't
binary = "binary"
do_not = "don't"
# define y, a string about those that know binary and those that don't
y = f"Those who know {binary} and those who {do_not}."

# Ouput x and y, the number of people there are
print(x)
print(y)

# Repeat the output in a an f-string format
print(f"I said: {x}")
print(f"I also said: {y}")

# Set the state of the hilarious variable
hilarious = False

# define A string stating the evaluation of the joke
joke_evaluation = "Isn't that joke so funny?! {}"

# Output the joke evaluation wtih the current impression
print(joke_evaluation.format(hilarious))

#Set additional strings for practice
w = "This is the left side of..."
e = "a string with a right side."

# Output these strings in sequence.
# Be sure to get the sequence right
print(w + e)

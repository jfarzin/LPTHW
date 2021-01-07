# Here's some new strange stuff, remember type it exactly. 

# define variable for days
days = "Mon 'Tue' Wed Thu Fri Sat Sun"
# define variable 'months'
# \ = escape
# use '\n' for a line break in a string
# use \" to allow the quotes inside a string
months = "\nJan\nFeb\n\"Mar\nApr\nMay\nJun\nJul\nAug"

# print the days by calling days variable
print("Here are the days: ", days)
# print months by calling months variable
print("Here are the months: ", months)
# notice formatting differences among strings

# print a block of unbounded text as a string
print("""
There's something going on here.'
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


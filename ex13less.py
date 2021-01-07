from sys import argv
script, first, second = argv

print("The script is called", script)
print(f"This is the {script} script.")
if (str.isnumeric(first) and str.isnumeric(second)):
    the_sum = float(first) + float(second)
#only want to do this if they are actual numbers
#guess I'll figure out how to check later
print("Combining the text yields:", first + second, end = " ")
print("but the sum is", the_sum)
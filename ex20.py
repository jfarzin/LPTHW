from sys import argv

#assign the arguments that we got from the command line
#to variables
script, input_file = argv

#write a function
#take a parameter and print out all it's contents
def print_all(f):
    print(f.read())

#write a function that goes back to the start of the file
#where the file is the parameter passed as f
def rewind(f):
    f.seek(0)

#write a function
#that prints one line at a time
#needs two parameters, the line to read and the file
def print_a_line(line_count, f):
    #print the line number and the line itself
    print(line_count, f.readline(), end="")

#assign the file that we got in the argument as the current file
#and open it
current_file = open(input_file)

#tell what we are going to do next
print("First, let's print the whole file:\n")

#call the print_all function
#pass it the current_file parameter
print_all(current_file)

#tell what we are going to do
print("Now let's rewind, kind of like a tape.")

#call the rewind function and set the location in the file to the start
rewind(current_file)

#tell what we are gong to do
print("Let's print three lines:")

#set the current_line to 1
current_line = 1
#for debugging: print(f">>> current line {current_line}")
#call the function to print just one line at at time
#set two parameters - the line to print and the file itself
print_a_line(current_line, current_file)

#increase the current_line by 1 (always 2 here)
current_line = current_line + 1
#for debugging: print(f">>> current line {current_line}")
#call the function to print just one line at at time
#set two parameters - the line to print and the file itself
print_a_line(current_line, current_file)

#increase the current line by 1 (always 3 here)
current_line += 1
#for debugging: print(f">>> current line {current_line}")
#call the function to print just one line at a time
#set two parameters - the line to print and the file itself
print_a_line(current_line, current_file)



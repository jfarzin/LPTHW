#bring the 'argument vector' feature into our script
from sys import argv

#we give two arguments when we run the script in python. 
# assign these two script and filename variables, respectively
script, filename = argv

#open the file passed in the argument (above) 
#and assign the content of the file to our variable txt
txt = open(filename)

#tell us what file we are going to read
print(f"Here's your file {filename}:")
#then print the content of the file, by 
#opening the txt of the file and reading all of it 
print(txt.read())

#close the file
txt.close()

#ask for a new filename (or the same again)
print("Type the filename again:")
#assign the input given from our last prompt to 'file_again'
file_again = input("> ")

#for the most recent filename, open the file and save
#the contents to the variable txt_again
txt_again = open(file_again)

#print out the contents of that most recent file by
#reading the saved text
print(txt_again.read())

#close the most recent file
txt_again.close()

from sys import argv
#read the WYSS for how to run this
num_kids = int(input("How many children do you have?"))
script, first, second, third, fourth = argv

#for 1 to num_kids
# would like to create argument names based on number of kids 
#and then print them as appropriate
#so that the script would be more flexible
#guess we'll get there...   

#print("The script is called:", script)
print("My oldest child is:", first)
print("My second child is:", second)
print("My third child is:", third)
print("My baby is:", fourth)

print("Give me a filename, already")
thefile = input(">>> ")

txt = open(thefile)
print(txt.read())
print(f"There it is: {thefile}.")

txt.close()

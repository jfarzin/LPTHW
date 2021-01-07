#looked up an example of how to bound the data
#that I am collecting from the input()
#here, must be between 1-26
#example from stack overflow "limiting user input to a range"

shift = 0
while not int(shift) in range(1,27):
    shift = input("Please enter your shift (1-26): ")
print(f"You are working shift {shift}.")

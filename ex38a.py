ten_things = "Apples Oranges Crows Telephone Light Sugar"
#ten_things = "Apples Oranges"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
                "Corn", "Banana"]

i = ten_things.count 

for i in range(len(stuff),10):
    if len(stuff) < 10:
        next_one = more_stuff.pop(0)
        print("Adding: ", next_one)
        stuff.append(next_one)
        #more_stuff.append(next_one)
        print(f"There are {len(stuff)} items now.")
next 

'''
while len(stuff) != 8:
    next_one = more_stuff.pop(0)
    print("Adding: ", next_one)
    stuff.append(next_one)
    #more_stuff.append(next_one)
    print(f"There are {len(more_stuff)} items now.")
'''

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print(','.join(stuff[3:5])) # super stellar!
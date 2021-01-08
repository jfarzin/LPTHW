lift_routes = ["Black", "Fraser", "Red", "Rec Center", "Green",
                    "West Fraser Express", "Purple", "Meadowridge Express"]
'''
#test sample list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''

#use print statements to debug

routes = []
destinations = []

for x in lift_routes:
    #print(x)
    nextroute = lift_routes.pop(0)
    routes.append(nextroute)
    #print(f"routes has {len(routes)} items now.")
    nextdest = lift_routes.pop(0)
    destinations.append(nextdest)
    #print(f"destinations has {len(destinations)} items now.")

'''
for y in routes:
    print(' '.join(y)) 

for z in destinations:
    print(' '.join(z)) 
'''

print("Assignment: do something with a real life list:")

#this was broken because i didn't need first range param and was missing f and brackets in print statements
#for i in range(0,len(routes)):
#    print(routes(i))
    #print("The {routes(i)} Line is the {destinations(i)}.")


#got it:
for x in range(len(routes)): 
    #print(f"the {routes[x]} line.")
    print(f"The {routes[x]} line is the {destinations[x]} line.")




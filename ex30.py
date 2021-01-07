people = 9
cars = 8
trucks = 15

#practicing debug print statements. 
#print(f">>>>eval people ({people}) and cars ({cars})")
if cars > people and people > 0:
    #print(f">>{cars} > {people} and {people} > 0")
    print("We should take the cars.")
elif cars < people and people > 0:
    #print(f">>{cars} < {people} and {people} > 0")
    print("We should not take the cars.")
else:
    #print(f">>{cars} = {people} or {people} = 0")
    print("We can't decide.")

#print(f">>>>eval cars ({cars}) and trucks ({trucks})")
if trucks > cars:
    #print(f">>{trucks} > {cars}")
    print("That's too many trucks.")
elif trucks < cars:
    #print(f">>{trucks} < {cars}")
    print("Maybe we could take the trucks.")
else:
    #print(f">>{trucks} = {cars}")
    print("We still can't decide.")

#print(f">>>>eval people ({people}) and trucks ({trucks})")
if people > trucks:
    #print(f">>{people} > {trucks}")
    print("Alright, let's just take the trucks.")
else:
    #print(f">>{people} <= {trucks}")
    print("Fine, let's stay home then.")

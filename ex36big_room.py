
def big_room(balloons):
    print("""
    Strange enough, Pooh and Piglet are walking in 
    circles around the room.
    Hmm, you wonder what they could be doing. You
    ...bravely follow them?
    ...collect Oliver's babies and put them in his crib?
    ...start folding the laundry?
    """)

    choice = input(">> ")


    if "follow" in choice:
        #you bravely join them
        print("""
        \"Help!\" cried Piglet \"A Heffalump! A Horrible Heffalump!\"
        You know that Heffalumps are very fierce with
        bears and pigs, and maybe even children!
        \"Oh, dear! Oh, dear\", you mumble...louder and louder.
        """)
        #mom() 
        #straight_to_bed()
    elif "babies" in choice:
        print("""
        As you are picking up Oliver's babies, you 
        notice something like a bell-rope on the floor.
        Wait, that's Eeyore's tail!
        Christopher Robin can put it back on again.
        """)
        #go to the bedroom (find Christopher Robin there)
    elif "laundry" in choice:
        print("""
        While you are folding laundry, you call to turn 
        on some music. Who comes to help: mom or dad?
        """)
        parent = input(">> ")

        #random # generator, if = x ==> dance party
        if parent =="mom":
            print("fill in this")
            #fold laundry together. no music, baby sleeping
            #if random # ==> dance party   
        elif parent == "dad":
            print("fill in this")
            #grateful dead. 
            #random # ==> jazz party
        else:
            print("I'm a Pooh of very little brain; i didn't get that.")
            #mom()

    else:
        print("fill in this")   
        #pooh of little brain, start over.

    #start folding the laundry
    #ask mom if you can turn on music
        #dance party.  if balloons > 2 ==> unexpected errand
    
    
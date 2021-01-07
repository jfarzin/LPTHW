print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

def when_frightened(choice):
    #print(">>> choice:", choice)
    choice = int(choice)
    if choice == 1:
        print("You enter into a dream world of animals everywhere eating cake. Good job!")
    elif choice == 2:
        print("You wake up. Phew!")
    elif choice == 3:
        print("Embrace the bear and start dancing. Lovely.")    
    elif 3 < choice <  10:
        print("Hmm. Good luck with that.")
    elif choice in range(10,20):
        print("Yowsers!", choice)
    else:
        print(f"No, {choice} is an invalid option. Choose 1-9?")
        frightened = input("> ")
        when_frightened(frightened)
        


if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Run back to the door.")

    bear = input("> ")

    if bear == "1":
        print("You and the bear share the cake. Good job!")
    elif bear == "2":
        print("The bear gets frightened and chases you. You...")
        print("1. Run deep into the cave away from the bear.")
        print("2. Stumble and fall.")
        print("3-19. Gamble with your future. Stand your ground.")

        frightened = input("> ")
        when_frightened(frightened)

    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")
    
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")



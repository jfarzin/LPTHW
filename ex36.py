#Exercise 36: Make a game!
#The Farzin Bedtime Challenge
#Can you avoid distractions and get to bed on time?

from sys import exit
import random

def mom_coming():
    rand = random.uniform(0,1)
    if rand <= 0.65:
        print("\tMom is coming.")
    else:
        print("\tDad is coming.")
    
def try_again():
    print("Oops! I am a bear of little brain. Try again!")

def straight_to_bed():
    print("\tWhat is all that ruckus!")
    print("\tYou are going straight to bed!\n\n")
    exit(0)

def find_list_index(var):
    room_index = 0
    for rmlist in chore_list:
        chore_index = 0    
        for chore in rmlist:
            
            if chore == var:
                return(room_index, chore_index + 1)
            else:
                chore_index += 1
        
        room_index += 1

def brush_teeth():
    print("Do you need mom/dad to help you brush?")
    print("1 for yes, 2 for no.")
    
    help = input(">> ")
        
    try:
        help = int(help)
                
        if help == 1:
            print("You said you need help.")
            mom_coming()
            # add options
        elif help == 2:
            print("You said you don't need help. But...")
            mom_coming() 
            # add options
        else:
            try_again()
            brush_teeth()
            
    except ValueError:
        try_again()
        brush_teeth()
    
def kitchen(kitchen_clean, balloons):
    #print(f">>> start clean: {kitchen_clean} and balloons: {balloons}")
    print("""
    There is quite a commotion on the balcony. 
    Will you...
    ...bring your plate to the sink? (1)
    ...help mom and dad clean the table and floors? (2)
    ...check the balcony really quickly? (3)
    """)    

    #while True 
    #add this while after all exit options given below, except last
    choice = input(">> ")

    if choice == "1":
        print("Thank you so much.")
        print("Please just put it directly into the dishwasher.")
        balloons += 1
        
        #need to choose where to go next
    elif choice == "2":
        print("""
        Thank you so much!
        When you are done, mom and dad give you
        a honey popsicle to eat on the balcony!
        Oh look! Pooh is already here, 
        eating honey with rabbit. :)
        What a beautiful evening to sit outside with friends.
        """)
        balloons += 2
        kitchen_clean = 1
        #need to choose where to go next
    elif choice == "3":
        print("""
        Is that Pooh eating honey on the balcony?
        But when you open the door, you get stung by a bee!
        OUCH!
        Oh bother!
        """)
        mom_coming()
        straight_to_bed()
    else:
        print("Oops. I am a bear of little brain. Try again!")
        kitchen_clean, balloons = kitchen(kitchen_clean, balloons)

    #print(f">>> end clean: {kitchen_clean} and balloons: {balloons}")
    return kitchen_clean, balloons

def bathroom(bathroom_list):
    #print(">>>> bath list begin: ", bathroom_list[:])
    brushed_teeth, used_potty, balloons = bathroom_list

    print("""
    Oh my goodness - Kanga is scrubbing Piglet
    with a large lathery flannel! 
    \"Ow! Let me out!\" cries Piglet.
    \"Don't open your mouth dear or soap goes in...\"
    says Kanga.
    What should you do?
    ...start to brush your teeth right away?
    ...quietly use the potty?
    ...try to save Piglet?
    """)
    
    choice = input(">> ")

    if "teeth" in choice and brushed_teeth == 1:
        print("Didn't you already brush your teeth?")
        #give other options
    elif "teeth" in choice and brushed_teeth == 0: 
        balloons += 1
        brushed_teeth = 1
        brush_teeth()
    elif "potty" in choice:
        print("Be quick now.")
        used_potty = 1
        # add options here bathroom, kitchen, big_room     
    elif "piglet" in choice:
        print(""" 
        \"Don't say a word! There goes the soap!\" says Kanga.
        Oh my - Kanga looks up and grabs you before you can 
        help at all! Into the cold bath you go!
        """)
        mom_coming()
        straight_to_bed()
        exit()
    else:
        try_again() #put this input in a while loop also?
        #add options bathroom(bathroom_list)

    bathroom_list = [brushed_teeth, used_potty, balloons]
    #print(">>>> bath list end: ", bathroom_list[:])
    return bathroom_list

def how_many_balloons(balloons):
    if balloons == 1:
        print(f"You now have {balloons} balloon.\n")
    else:
        print(f"You now have {balloons} balloons.\n")

def intro_text():
    print("""Oh joy! Several friends have stopped 
    in for a visit... but it's awfully late!  Can 
    you follow the rules and get ready for bed? 
    If you get distracted and goof off, you will 
    be sent straight to bed!  But if you can 
    successfully complete your tasks, you will
    be rewarded with a wonderful prize!\n\n
    You...  
    ...Stay in the kitchen? 
    ...Go to the bathroom?
    """) 
    

def start(new_game, kitchen_clean, balloons, bathroom_list):
    
    if new_game == 0:
        intro_text()
        new_game = 1
    else:
        print(""" 
        You...  
        ...Go to the kitchen? 
        ...Go to the bathroom?
        """) 
    #add these choices as available
    #...Wander into the big room?
    #...Or go to your bedroom?
    

    choice = input("> ")

    if "kitchen" in choice and kitchen_clean == 0:
        kitchen_clean, balloons = kitchen(kitchen_clean, balloons)
    elif "kitchen" in choice and kitchen_clean == 1:
        print("Kitchen is clean! I think you meant bathroom.")
        bathroom_list = bathroom(bathroom_list)
    elif "bath" in choice: 
        bathroom_list = bathroom(bathroom_list)
    #elif "bed" in choice:
        #bedroom()
    #elif "big" in choice:
        #big_room()
    else:
        mom_coming()
        try_again()
        exit()

    return new_game, kitchen_clean, balloons, bathroom_list

def almost_there(balloons):
    print("""
    Don't get distracted, keep moving toward bed.
    Will you...
    ...check to see if there are packages outside?
    ...sit on the couch and wait for a book?
    ...see what your brother is doing?
    """)

    choice = input(">> ")

    if "book" in choice or "couch" in choice:
        print("\tChristopher Robin will read a story to you!")
        success(balloons)
    elif "check" in choice or "package" in choice:
        print("\tOh, look, it's a present from Vovi!")
        #continue playing
        #open package or save for morning
        #it's a hairbrush, outfit from Costco, new goggles, stickers, sheets!
        exit()
    else:
        mom_coming()
        straight_to_bed()
        exit()
    
def success(balloons): 
    #add something about # balloons to keep and play
    #with tomorrow
    print(f"""
    Congratulations!  
    You successfully avoided all the trips and traps! \n 
    You can put your {balloons} balloons 
    in a special place for safe-keeping. \n   
    And as a reward for following all the rules...\n 
    Pooh and his friends will tuck you in, and stay
    with you tonight. And tomorrow, you will join them
    on an...
    \tExpotition to the North Pole!!!\n
    Sweet dreams. I love you. Good night.\n\n
    """)
    exit(0)


'''new_game = 0
balloons = 0
kitchen_clean = 0

teeth_brushed = 0
used_potty = 0
bathroom_list = [teeth_brushed, used_potty, balloons]

pjs_on = 0
toys_cleaned_up = 0
'''

new_game = 0
balloons = 0
user = "Name"
total_chores = 0
basics = ["new_game", new_game, "balloons", balloons, "user", user, "total_chores", total_chores]

kitchen_cleaned = 0
take_probiotics = 0
kitchen_list = ["kitchen_cleaned", kitchen_cleaned, "take_probiotics", take_probiotics]

teeth_brushed = 0
used_potty = 0
bathroom_list = ["teeth_brushed", teeth_brushed, "used_potty", used_potty]

pjs_on = 2
make_bed = 12
bedroom_list = ["pjs_on", pjs_on, "make_bed", make_bed]

toys_cleaned_up = 0
checked_for_packages = 0
laundry_folded = 0
read_books = 0
bigroom_list = ["toys_cleaned_up", toys_cleaned_up, "checked_for_packages", checked_for_packages, "laundry_folded", laundry_folded, "read_books", read_books]

chore_list = [basics, kitchen_list, bathroom_list, bedroom_list, bigroom_list]



while True:
    
    r, c = find_list_index("kitchen_cleaned")
    kitchen_cleaned = chore_list[r][c]
    r, c = find_list_index("teeth_brushed")
    teeth_brushed = chore_list[r][c]
    r, c = find_list_index("balloons")
    balloons = chore_list[r][c]

    if kitchen_clean == 1 and teeth_brushed == 1:
        almost_there(balloons)
    else:
        #chore_list = start(chore_list)
        
        new_game, kitchen_clean, balloons, bathroom_list = start(new_game, kitchen_clean, balloons, bathroom_list)
        #replace all these inside start function

        #use lookup function to replace values
        teeth_brushed = bathroom_list[0]
        balloons = balloons + bathroom_list[2]

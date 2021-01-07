from sys import exit

def bathroom(bathroom_done, balloons):
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

    if choice == "brush teeth":
        balloons += 1
        print("Do you need mom/dad to help you brush?")
        print("1 for yes, 2 for no.")
        help = input(">> ")
        
        if help.isnumeric() == True:
            help = int(help)
        if help == 1:
            print("You said you need help.")
            mom()
        elif help == 2:
            print("You said you don't need help.")
            mom()
        else:
            brush_teeth 
        
        bathroom_done = 1
        
    elif choice == "use potty":
        print("Be quick now.")
        bathroom(bathroom_done, balloons)     
    elif choice == "save piglet":
        print(""" 
        \"Don't say a word! There goes the soap!\" says Kanga.
        Oh my - Kanga looks up and grabs you before you can 
        help at all! Into the cold bath you go!
        """)
        mom()
        straight_to_bed()
        exit()
    else:
        print("Oops. You or Pooh - one of you has no brain. Try again!")
        bathroom(bathroom_done, balloons)

    return balloons

# add subsequent choices for after bathroom...


def mom():
    print("Mom is coming.")

def straight_to_bed():
    print("What is all that ruckus! You are going straight to bed!")

bathroom_done = 0
balloons = 0
bathroom_done, balloons = bathroom(bathroom_done, balloons)
if balloons == 1:
    print(f"You now have {balloons} balloon.")
else:
    print(f"You now have {balloons} balloons.")
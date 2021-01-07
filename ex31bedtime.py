def brush_teeth():
    print("Do you need mom/dad to help you brush?")
    print("1 for yes, 2 for no.")
    help = input(">> ")
    if help.isnumeric() == True:
        help = int(help)
    if help == 1:
        print("You said you need help.")
    elif help == 2:
        print("You said you don't need help.")
    else:
        brush_teeth 
    print("Mom is coming.")
    
brush_teeth()

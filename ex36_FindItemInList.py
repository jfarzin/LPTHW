new_game = 0
balloons = 0
kitchen_cleaned = 0
take_probiotics = 0
kitchen_list = ["kitchen_cleaned", kitchen_cleaned, "take_probiotics", take_probiotics]

teeth_brushed = 0
used_potty = 0
bathroom_list = [teeth_brushed, used_potty, balloons]

pjs_on = 2
make_bed = 12
bedroom_list = ["pjs_on", pjs_on, "make_bed", make_bed]

toys_cleaned_up = 0
checked_for_packages = 0
laundry_folded = 0
read_books = 0
bigroom_list = [toys_cleaned_up, checked_for_packages, laundry_folded, read_books]

chore_list = [kitchen_list, bathroom_list, bedroom_list, bigroom_list]


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
        

var = "pjs_on"
room, chore = find_list_index(var)
print(">>>var: ", var)
print(chore_list[room][chore])
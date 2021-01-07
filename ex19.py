#define function cheese&crackers, which has two parameters
#this function will print out how many cheeses 
#and crackers we have
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
#end the function by dedenting

print("We can just give the function numbers directly:")
#call the function, use numbers as the parameters
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
#define variables for the amount of cheese and crackers we have
amount_of_cheese = "hello"
amount_of_crackers = 50

#call the function and use variables as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
#call the function and let the computer calculate the variables
cheese_and_crackers(10 + 20 , 5 + 6)

print("And we can combine the two, variables and math:")
#call the function
#function will combine the string
cheese_and_crackers(amount_of_cheese + "100", amount_of_crackers + 1000)

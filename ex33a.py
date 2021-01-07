var = 6
increment = 2
numbers = []

def build_list(list, cur_num):
    list.append(cur_num)
    print("Numbers now:", numbers)
    

for i in range(0, var, increment):
    #print(">>> starting i: " , i )
    #print(f"In the for loop, i is {i}")
    i = build_list(numbers, i)
    #print(">>> ending i: " , i )


print("The full list of numbers is: ")

for num in numbers:
    print(num)

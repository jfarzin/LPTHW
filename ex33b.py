
def build_list(i, list, upper_bound, increment):
    #print(">>> i:", i, "and upper bound", upper_bound)
    if i < upper_bound:
        list.append(i)
        i += increment
        build_list(i, list, upper_bound, increment)

start = 0
numbers = []
upper_bound = 10
increment = 3

build_list(start, numbers, upper_bound, increment)

print("The numbers: ", numbers)

for num in numbers:
    print(num)

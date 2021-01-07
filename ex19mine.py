def farzin_family(p, c, g, o):
    print(f"""
    There are many ways to classify the Farzin kids:
    {p}, {c}, {g}, and {o}.
    """)

farzin_family("Parvis", "Clara", "Graham", "Oliver")

ageP = 9
ageC = 7
ageG = 5
ageO = 1.9
farzin_family(ageP, ageC, ageG, ageO)

farzin_family(1, 2, 3, 4)
farzin_family("biggest", "bigger", "smaller", "smallest")

Parvis = "big"
Clara = "big"
Graham = "small"
Oliver = "small"
farzin_family(Parvis, Clara, Graham, Oliver)

farzin_family("Parvis"+Parvis, "Clara"+Clara, "Graham"+Graham, "Oliver"+Oliver)
farzin_family(ageP*ageP, ageC*ageC, ageG*ageG, ageO*ageO)
farzin_family(ageP*1, ageC*2, ageG*3, ageO*4)

orderP = 1
orderC = 2
orderG = 3
orderO = 4
farzin_family(orderP, orderC, orderG, orderO)
farzin_family(ageP + orderP, ageC + orderC, ageG + orderG, ageO + orderO)

Parvis = "silly"
Clara = "fun"
Graham = "imaginative"
Oliver = "present"
farzin_family(Parvis, Clara, Graham, Oliver)

Parvis = "choochoo"
Clara = "uh-oh"
Graham = "Hi!"
Oliver = "tickle, tickle"
farzin_family(Parvis, Clara, Graham, Oliver)

Parvis = "creamed spinach"
Clara = "pate"
Graham = "eggs"
Oliver = "liver formula"
farzin_family(Parvis, Clara, Graham, Oliver)

#kids = ["Parvis", "Clara", "Graham", "Oliver"]
#For  in kids:
#(not yet just wait for loops)
Parvis = input("Give me one word to describe Parvis: ")
Clara = input("Give me one word to describe Clara: ")
Graham = input("Give me one word to describe Graham: ")
Oliver = input("Give me one word to describe Oliver: ")
farzin_family(Parvis, Clara, Graham, Oliver)

farzin_family("Parvis", "Clara", "Graham", "Oliver")

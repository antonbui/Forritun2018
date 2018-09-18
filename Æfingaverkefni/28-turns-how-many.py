turns = int(input("How many times do you want to write a new number? "))
pcount = 0
ncount = 0

for i in range(turns):
    newturn = int(input("Input a number: "))
    if newturn > 0:
        pcount += 1
    if newturn < 0:
        ncount += 1

print("You picked positive numbers", pcount, "times")
print("You picked negative numbers", ncount, "times")
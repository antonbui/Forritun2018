turns = int(input("How many times do you want to write a new number? "))
pcount = 0
ncount = 0
psum = 0
nsum = 0

for i in range(turns):
    newturn = int(input("Input a number: "))
    if newturn > 0:
        pcount += 1
        psum += newturn
    if newturn < 0:
        ncount += 1
        nsum += newturn

print("You picked positive numbers", pcount, "times and the sum is:", psum)
print("You picked negative numbers", ncount, "times and the sum is:", nsum)
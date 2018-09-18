turns = int(input("How many times do you want to write a new number? "))
count = 0

for i in range(turns):
    newturn = int(input("Input a number: "))
    if newturn < 0:
        count += 1

print("You picked negative numbers", count, "times")
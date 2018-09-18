turns = int(input("How many times do you want to write a new number? "))

for i in range(turns):
    newturn = int(input("Input a number: "))
    if (newturn%2) == 1:
        print("You picked: ", newturn)
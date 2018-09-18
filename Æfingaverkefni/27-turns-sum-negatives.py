turns = int(input("How many times do you want to write a new number? "))
result = 0

for i in range(turns):
    newturn = int(input("Input a number: "))
    if newturn < 0:
        result += i

print("The sum of the negative numbers is", result)
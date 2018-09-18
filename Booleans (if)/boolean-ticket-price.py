age = int(input("Input age: ")) # Do not change this line

# Fill in the missing code below
price = 30.0

if age >= 65:
    price = price / 2
    print(price)
elif age <= 5:
    price = 0.0
    print(price)
elif age < 0:
    print("Invalid age")
else:
    print(price)

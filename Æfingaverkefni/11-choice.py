a = int(input("Input a number: "))
b = int(input("Input another number: "))
choice = int(input("Choose 1 for addition, 2 for subtraction and 3 for multiplication: "))

if choice == 1:
    print(a + b)
elif choice == 2:
    print(b - a)
elif choice == 3:
    print(a * b)
else:
    print("Invalid input")


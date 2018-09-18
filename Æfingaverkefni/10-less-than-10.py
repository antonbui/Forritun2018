num = int(input("Input a number: "))

if num < 10 and num >= 0:
    print("Less than 10")
elif num >= 10 and num < 20:
    print("Between 10 and 20")
elif num >= 20:
    print("Value is too high")
elif num < 0:
    print("too low")
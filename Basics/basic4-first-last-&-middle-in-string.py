x_str = input("Input x: ")
# remember to convert to an int
x = int(x_str)
first_three = x // 1000
last_two = x % 100
middle_two = x // 100 % 100
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)

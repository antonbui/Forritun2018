# The function definition goes here
def inrange(number):
    if number > 1 and number < 555:
        return True

num = int(input("Enter a number: "))

# You call the function here
if inrange(num) == True:
    print(num, "is in range.")
else:
    print(num, "is outside the range!")
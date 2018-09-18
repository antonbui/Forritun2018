n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
number = 2
count = 0
prime = True

while number < n:
    if n % number == 0:
        prime = False
    number += 1
    if count == 0:
        break

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("!Prime")
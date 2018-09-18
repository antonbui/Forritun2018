# is_prime function definition goes here
def is_prime(n):
    number = 2
    prime = True

    while number < n:
        if n % number == 0:
            prime = False
        number += 1

    return prime

num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
primenum = is_prime(num)

if primenum == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime")
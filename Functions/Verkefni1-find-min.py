# find_min function definition goes here
def find_min(s1, s2):
    if s1 > s2:
        s1 = s2
    return s1

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
# Call the function here
minimum = find_min(first, second)
print("Minimum: ", minimum)
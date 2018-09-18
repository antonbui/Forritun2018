# Your function definition goes here

def count_case(mystr):
    countupper = 0
    countlower = 0
    for i in mystr:
        if i.isupper():
           countupper += 1
        elif i.islower():
            countlower += 1
    return countupper, countlower


user_input = input("Enter a string: ")

# Call the function here
upper, lower = count_case(user_input)

print("Upper case count: ", upper)
print("Lower case count: ", lower)
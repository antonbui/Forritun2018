s = input("Input a string: ")

digits = ""

for i in s:
    if i.isdigit():
        digits += i
print(digits)

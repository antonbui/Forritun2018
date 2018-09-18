# palindrome function definition goes here

def palindrome(mystr):
    mystr = mystr.lower()
    newstr = ""
    for i in mystr:
        if i.isalpha():
            newstr += i
         
    if newstr == newstr[::-1]:
        return True
    else:
        return False




in_str = input("Enter a string: ")

# call the function and print out the appropriate message

pal = palindrome(in_str)

if pal == True:
    print(f'"{in_str}" is a palindrome.')
else:
    print(f'"{in_str}" is not a palindrome.')
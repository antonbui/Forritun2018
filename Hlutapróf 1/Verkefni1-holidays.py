month = input("Month: ")
day = int(input("Day: "))

mystr = month.capitalize() + " " + str(day)

if mystr == "January 1":
    print("New year's day")
elif mystr == "June 17":
    print("National holiday")
elif mystr == "December 25":
    print("Christmas day")
else:
    print("Not a holiday")
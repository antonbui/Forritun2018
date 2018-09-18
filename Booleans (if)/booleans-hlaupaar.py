year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below


if (year % 4) == 0:
    
        if (year % 100) == 0 and (year % 400) != 0:
        
            print (False)
        
        else:
            print(True)
        
else:
    print(False)

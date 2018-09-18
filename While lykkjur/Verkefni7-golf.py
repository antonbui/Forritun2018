hole = 1
while hole <= 18:
    par = int(input("Par of hole " + str(hole) + ": "))
    score = int(input("Score on hole " + str(hole) + ": "))
    
    if par >= 3 and par <= 5:
        if score  <= par - 4:
            print("invalid score")
        if score == par - 3:
            print("albatross")
        if score == par - 2:
            print("eagle")
        if score == par - 1:
            print("birdie")
        if score == par:
            print("par")
        if score == par + 1:
            print("bogey")
        if score == par + 2:
            print("double bogey")
        if score == par + 3:
            print("triple bogey")
        if score >= par + 4:
            print("bad hole")
    else:
        print("Invalid input on par")
    hole += 1

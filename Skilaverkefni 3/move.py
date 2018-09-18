
def message():
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")

def charactermove(pos):
    message()
    choice = input("Input your choice: ")
    if choice == "l":
        if pos == 1:
            newposition = pos
            print("New position is:", newposition)
            charactermove(newposition)
        else:
            newposition = pos - 1
            print("New position is:", newposition)
            charactermove(newposition)
    elif choice == "r":
        if pos == 10:
            newposition = pos
            print("New position is:", newposition)
            charactermove(newposition)
        else:
            newposition = pos + 1
            print("New position is: ", newposition)
            charactermove(newposition)
    else:
        newposition = pos
        print("New position is:", newposition)
        

    

startposition = int(input("Input a position between 1 and 10: "))

charactermove(startposition)
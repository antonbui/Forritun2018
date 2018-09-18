
def message():
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")
pos = 0
def charactermove(pos):
    message()
    choice = input("Input your choice: ")
    if choice == "l":
        if pos == 1:
            newpos(0)
        else:
            newpos(-1)
    elif choice == "r":
        if pos == 10:
            newpos(0)
        else:
            newpos(1)
    else:
        newposition = pos
        print("New position is:", newposition)
        
def newpos(n):
    newposition = charactermove(pos) + n
    print("New position is: ", newposition)
    charactermove(newposition)

    

startposition = int(input("Input a position between 1 and 10: "))

charactermove(startposition)

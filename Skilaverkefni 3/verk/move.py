
def message():
    print("""l - for moving left
r - for moving right
Any other letter for quitting""")

def left(pos):
    if pos == LOWER:
        newposition = pos
        return newposition
    else:
        newposition = pos - 1
        return newposition

def right(pos):
    if pos == UPPER:
        newposition = pos
        return newposition
    else:
        newposition = pos + 1
        return newposition
        
start = int(input("Input a position between 1 and 10: "))

UPPER = 10
LOWER = 1

while True:
    message()
    choice = input("Input your choice: ")
    if choice == "l":
       left(start)
       start = left(start)
       print("New position is:", start)
    elif choice == "r":
        right(start)
        start = right(start)
        print("New position is:", start)
    else:
        print("New position is:", start)
        break

victory = False
position = 1.1
direction = ""

while not victory:
    
    if position == 1.1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction in ["N", "n"]:
            position += 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction")
    elif position == 1.2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction in ["N","n"]:
            position += 0.1
            position = round(position, 2)
        elif direction in ["E", "e"]:
            position += 1.0
            position = round(position, 2)
        elif direction in ["S", "s"]:
            position -= 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")
    elif position == 1.3:
        print("You can travel: (E)ast or (S)outh.")
        direction = input("Direction: ")
        if direction in ["E", "e"]:
            position += 1.0
            position = round(position, 2)
        elif direction in ["S", "s"]:
            position -= 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")

    elif position == 2.1:
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction in ["N", "n"]:
            position += 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")
    elif position == 2.2:
        print("You can travel: (W)est or (S)outh.")
        direction = input("Direction: ")
        if direction in ["W", "w"]:
            position -= 1.0
            position = round(position, 2)
        elif direction in ["S", "s"]:
            position -= 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")
    elif position == 2.3:
        print("You can travel: (W)est or (E)ast.")
        direction = input("Direction: ")
        if direction in ["E", "e"]:
            position += 1.0
            position = round(position, 2)
        elif direction in ["W", "w"]:
            position -= 1.0
            position = round(position, 2)
        else:
            print("Not a valid direction.")

    elif position == 3.1:
        print("Victory!")
        victory = True
    elif position == 3.2:
        print("You can travel: (N)orth or (S)outh.")
        direction = input("Direction: ")
        if direction in ["N", "n"]:
            position += 0.1
            position = round(position, 2)
        elif direction in ["S", "s"]:
            position -= 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")
    elif position == 3.3:
        print("You can travel: (W)est or (S)outh.")
        direction = input("Direction: ")
        if direction in ["W", "w"]:
            position -= 1.0
            position = round(position, 2)
        elif direction in ["S", "s"]:
            position -= 0.1
            position = round(position, 2)
        else:
            print("Not a valid direction.")
        
        

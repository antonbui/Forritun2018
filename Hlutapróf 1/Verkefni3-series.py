num = int(input("Initial value: "))
step = int(input("Step: "))

sequence = ""
sumofsequence = 0


while sumofsequence < 100:
    sumofsequence += num
    sequence = sequence + str(num) + " "
    nextnum = num + step
    num = nextnum
        
print(sequence)
print("Sum of series:", sumofsequence)

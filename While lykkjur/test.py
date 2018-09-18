top_num = int(input("Upper number for the range: ")) # Do not change this line
summa=0
for i in range (1,top_num+1):
    for j in range(1,i):
        if i % j == 0:
            summa += j
    if summa == i:
        print(i)
m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line


if m > n:
    m, n = n, m
for i in range(m,0, -1):
    if m % i == 0 and n % i == 0:
        print(i)
        break
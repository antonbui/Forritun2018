high = int(input("Input the higher number in a range: "))
low = int(input("Input the lower number number in a range: "))

if low < high:
    for i in range(low, high+1):
        print(i)
else:
    print("Error")
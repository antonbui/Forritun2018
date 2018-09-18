low = int(input("Input the lower number number in a range: "))
high = int(input("Input the higher number in a range: "))

if low < high:
    for i in range(low, high+1):
        result = i + i
    print(result + i)
        
else:
    print("Error")

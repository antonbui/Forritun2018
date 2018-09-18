low = int(input("Input the lower number number in a range: "))
high = int(input("Input the higher number in a range: "))
result = 0

if low < high:
    for i in range(low, high+1):
        if i%2 == 1:
            result += i
    print(result)
        
else:
    print("Error")

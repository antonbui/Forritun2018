low = int(input("Input the lower number number in a range: "))
high = int(input("Input the higher number in a range: "))
result = 0

if low < high:
    for i in range(low, high+1):
        if i%3 == 0:
            result += i
    print("The sum of all numbers divisable by 3 in the range is: ", result)
        
else:
    print("Error")

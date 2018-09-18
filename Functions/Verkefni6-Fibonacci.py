# Your function definition goes here

def fibonacci(n):
    a = 0
    b = 1
    sequence = ""
    for i in range(0, n):
        i = a
        a = b
        b = i + b
        sequence += str(a) + " "
    return sequence

n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here        

print(fibonacci(n))


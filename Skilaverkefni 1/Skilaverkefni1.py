cost = float(input("Input the cost of the item in $: "))
month = 0
payment = 50.0
remainder = cost
itotal = 0
if cost <= 1000:
    irate = 0.015
else:
    irate = 0.02

while True:
    month += 1
    interest = remainder * irate
    itotal += interest
    remainder += interest -payment
    if remainder > 0:
        print("Month:", month, "Payment:", round(payment, 2), "Interest paid:", round(interest, 2), "Remaining debt:", round(remainder, 2))
    else:
        payment += remainder
        remainder = 0.0  
        print("Month:", month, "Payment:", round(payment, 2), "Interest paid:", round(interest, 2), "Remaining debt:", round(remainder, 2), "\n")
        print("Number of months:", month,"\nTotal interest paid:", round(itotal,2))
        
        break

if cost < 0:
    print("error")
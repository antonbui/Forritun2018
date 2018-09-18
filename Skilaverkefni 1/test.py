cost = float(input("Input the loan amount: "))
month = 0
payment = 50.0
remainder = cost

if cost <= 1000:
    irate = 0.015
else:
    irate = 0.02

while True:
    month += 1
    interest = remainder * irate
    remainder += interest -payment
    if remainder > 0:
        print("Month:", month, "Payment:", round(payment, 2), "Interest paid: ", round(interest, 2), "Remaining debt: ", round(remainder, 2))
    else:
        payment += remainder
        remainder = 0   
        print("Month:", month, "Payment: ", round(payment, 2), "Interest paid: ", round(interest, 2), "Remaining debt: ", round(remainder, 2))
        break

if cost < 0:
    print("error")




elif cost > 1000:
    irate = 0.02
    month += 1
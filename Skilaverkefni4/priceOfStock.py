def shares(prompt, type):
    while True:
        try:
            sharenum = type(input(prompt))
            return sharenum
        except ValueError:
            print("Invalid number!")

def priceinp(sharenum):
    while True:
        try:
            price = input("Enter price (dollars, numerator, denominator): ")
            d, n, de = price.split()
            d, n, de = int(d), int(n), int(de)
            price = str(d) + " " + str(n) + "/" + str(de)
            return price
        except ValueError:
            print("Invalid price!")

def value(pricestr, sharenum):
    while True:
        try:   
            pricestr = pricestr.replace("/", " ")
            d, n, de = pricestr.split()
            value = (int(d) + (int(n) / int(de) ))*sharenum
            value = format(value, '.2f')
            return value
        except ValueError:
            print("Invalid price!")
            
def printout(numofshares, price, value):
    print(numofshares, "shares with market price", price, "have value $" + str(values))

def again():
    x = input("Continue: ")
    x = x.lower()
    if x != 'y':
        return False
    else:
        return True

a = True
while a == True:
    numofshares = shares("Enter number of shares: ", int)
    price = priceinp(numofshares)
    values = value(price, numofshares)
    printout(numofshares, price, value)
    a = again()
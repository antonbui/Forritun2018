sharenum = int(input("Enter number of shares: "))

price = input("Enter price, d, n, de: ")
d, n, de, = price.split()
price_str = d + " " + n + "/" + de


value = (int(d) + (int(n) / int(de) ))*sharenum

print(sharenum, "shares with market price", price_str, "have value $" + str(value))


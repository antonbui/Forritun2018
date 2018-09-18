s = input("Input a string: ")
# your code here

firstthree = s[0:3]
news = s.replace(firstthree, "")
print(news + firstthree)
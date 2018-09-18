s = input("Enter a sentence: ")

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

upper = 0
lower = 0
digits = 0
punct = 0

for i in s:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1
    if i.isdigit():
        digits += 1
    if i in punctuations:
        punct += 1


print("{:>15}".format("Upper case") + "{:>6}".format(upper))
print("{:>15}".format("Lower case") + "{:>6}".format(lower))
print("{:>15}".format("Digits") + "{:>6}".format(digits))
print("{:>15}".format("Punctuation") + "{:>6}".format(punct))
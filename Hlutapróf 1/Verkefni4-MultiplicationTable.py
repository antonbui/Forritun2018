first = ""
tvisvar = ""
þrisvar = ""
fjorum = ""
fimm = ""
sexs = ""
sjo = ""
atta = ""
niu = ""
tiu = ""


for i in range (1, 11):
    mystr = str(i * 1)
    first = first + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 2)
    tvisvar = tvisvar + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 3)
    þrisvar = þrisvar + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 4)
    fjorum = fjorum + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 5)
    fimm = fimm + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 6)
    sexs = sexs + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 7)
    sjo =sjo + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 8)
    atta = atta + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 9)
    niu = niu + " " + ("{:>4}".format(mystr))
for i in range (1, 11):
    mystr = str(i * 10)
    tiu = tiu + " " + ("{:>4}".format(mystr))

print(first)
print(tvisvar)
print(þrisvar)
print(fjorum)
print(fimm)
print(sexs)
print(sjo)
print(atta)
print(niu)
print(tiu)

#print("{:>12.2f}".format(s))


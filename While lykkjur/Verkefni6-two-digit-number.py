
teljari = 10
while teljari < 100:
    teljari += 1
    utkoma = teljari ** 2
    if utkoma > 1000:
        break
    sidustutveir = utkoma % 100
    if sidustutveir == teljari:
        print(teljari)

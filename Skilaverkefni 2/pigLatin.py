mystr = input("Enter a word: ")
while mystr != ("."):
    vowels = ("a", "e", "i", "o", "u")
    firstletter = mystr[0]
    if firstletter in vowels:
        piglatin = mystr + "yay"
    else:
        for i in mystr:
            if i in vowels:
                indx = mystr.index(i)
                break
        piglatin = mystr[indx:]+mystr[:indx] + "ay"
    print(piglatin)
    mystr = input("Enter a word: ")
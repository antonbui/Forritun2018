def clean(word):
    return word.strip().lower()

txtfile = open("words.txt", "r")
count = 0
for word in txtfile:
    word = clean(word)
    
    if len(word) > count:
        count = len(word)
        longest = word
    
print("Longest word is '" + longest +"' of length", count)

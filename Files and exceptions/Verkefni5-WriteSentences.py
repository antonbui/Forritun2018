def clean(word):
    word = word.strip()
    word.replace("\n", "")
    return word

txtfile = open("words.txt", "r")
sentences = open("sentences.txt", "w")
new_sent = ""
for word in txtfile:
    word = clean(word) + " "
    if word == ". ":
        word += "\n"
    elif word == " ":
        word = clean(word)
    new_sent += word
        
    
print(new_sent)
print(new_sent, file=sentences)

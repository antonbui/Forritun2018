name = input("Input a name: ")

last, first = name.split(", ")
first_initial = first.capitalize() + "."
last = last.title()

print(first_initial, last)
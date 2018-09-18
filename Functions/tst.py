number = 0x6F73

question_mask = number & 0x0780
answer_mask = number & 0x000C

question_number = question_mask >> 7
answer = answer_mask >> 2
if answer == 0:
    answer = "A" 
if answer == 1:
    answer = "B"
if answer == 2:
    answer = "C"
if answer == 3:
    answer = "D"

print("Question:", str(question_number))
print("Answer:", str(answer))
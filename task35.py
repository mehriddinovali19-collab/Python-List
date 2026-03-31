text = []
i = 1
while True:
    n = input(f"{i} - mantni kiriting: ")
    if n == "":
        break 
    text.append(n)
    i += 1


short_word = []
med_word = []
long_word = []

for w in text:
    if len(w) <= 3:
        short_word.append(w)
    elif 4<= len(w) <=6:
        med_word.append(w)
    elif len(w) > 6:
        long_word.append(w)

print(" short word:", short_word)
print("med words:", med_word)
print("long words:", long_word)

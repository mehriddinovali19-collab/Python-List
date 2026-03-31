text = []
i = 1
while True:
    n = input(f"{i} - mantni kiriting: ")
    if n == "":
        break 
    text.append(n)
    i += 1

longest_word = text[0]

for w in text:
    if len(w) > len(longest_word):
        longest_word = w
        

print("Eng uzun so'z:", longest_word)
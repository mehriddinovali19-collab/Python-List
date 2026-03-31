words = []
for i in range(5):
    n = input(f"{i+1} - Palindrom so'z kiriting: ")
    words.append(n)



new = []
for soz in words: 
    if soz[::-1] == soz:

     new.append(soz)


print("Natija: ", new)
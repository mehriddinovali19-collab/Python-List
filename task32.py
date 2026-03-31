words = []

for i in range(5):
    n = input(f"{i+1} - so'zni krirting: ")
    words.append(n)


new_list = []
for soz in words:
    if len(soz) > 5:
      new_list.append(soz)  

print("Natija: ", new_list)
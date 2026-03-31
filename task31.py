num = []
i = 1

while True:
    n = input(f"{i} - sonni kiriting: ")
    if n == "":
        break
    num.append(int(n))
    i += 1

max_count = 0
eng_kop = None

for son in num:
    if num.count(son) > 0:
        max_count = num.count(son)
        eng_kop = son


print("natija: ", eng_kop)
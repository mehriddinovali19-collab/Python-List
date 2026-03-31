list = []
list2 = [] 
print(" 1 - ro'yxatni kiriting")
i = 1
while True:
    n = input(f"{i} - elementni kiriting: ")
    if n == "":
        break
    list.append(n)
    i += 1

print("2 - ro'yxatni kiriting")
i = 1
while True:
    n = input(f"{i} - elementni kiriting: ")
    if n == "":
        break
    list2.append(n)
    i += 1

for i in range(len(list)):
    list[i], list2[i] = list2[i], list[i]

print("Yangi list1:", list)
print("Yangi list2:", list2)
number = []
for i in range(6):
    n = int(input(f"{i+1} - sonni kiriting: "))
    number.append(n)



    new_num = []
    for i in range(len(number)):
        for k in range(i+1, len(number)):
           if number[i] + number[k] == 10:
               new_num.append((number[i], number[k]))

print("Yig'indisi 10 ga teng juftliklar:", new_num)

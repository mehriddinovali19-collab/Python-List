sonlar = []
 
for i in range(10):
    n = input(f"{i+1} - sonni kiriting: ")


    sonlar.append(n)


# takorlanmaydigan sonlar

yangi =[]
for son in sonlar:
    if sonlar.count(son) == 1:

     yangi.append(son)


print("Natija: ", yangi)
list1 = [1, 2, 3, 4, 5] 
list2 = [4, 5, 6, 7]
common_list = []

for item in list1:
    if item in list2 and item not in common_list:
        common_list.append(item)

print("Umumiy ro'yxat: ", common_list)
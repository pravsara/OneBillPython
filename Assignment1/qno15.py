l = [x for x in input("Enter list : ").split(" ")]
print(set(l))
temp_list = []
for i in l:
    if i in temp_list:
        l.remove(i)
    elif i not in temp_list:
        temp_list.append(i)
print(temp_list)
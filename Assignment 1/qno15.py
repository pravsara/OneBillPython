l = [x for x in input("Enter list : ").split()]
print(set(l))
temp_list = []
for i in l:
    if i in l[l.index(i)+1:]:
        l.remove(i)
print(l)

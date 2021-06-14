from collections import OrderedDict as od
s = "mississippi"
print("".join(set(s)))  # using set to remove duplicates without order
print("".join(od.fromkeys(s)))
print("".join(sorted(set(s), key=s.index)))
temp_list = []
for i in s:
    if i not in temp_list:
        temp_list.append(i)
print(*temp_list, sep="")
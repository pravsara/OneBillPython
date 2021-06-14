n = int(input("Enter n : "))
print("Enter the Weights : ")
weight = []
for i in range(0, n):
    weight.append(int(input("Enter : ")))
set_weight = list(set(weight))
print("Average : ", sum(set_weight)/len(set_weight))
unique_list = []
for i in weight:
    if i not in unique_list:
        unique_list.append(i)
print("Average : ", sum(unique_list)/len(unique_list))
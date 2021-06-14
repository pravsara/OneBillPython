n = int(input('Enter no of elements:'))
dic = {}
for i in range(0, n):
    key, value = input('Enter Key and Value: ').split()
    dic[key] = int(value);
print(sum(dic.values()))
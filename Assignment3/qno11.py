n = int(input('Enter limit : '))
temp1 = 0
temp2 = 1
if n == 1:
    print(0)
if n == 2:
    print(1)
for i in range(2, n):
    temp3 = temp1 + temp2
    temp1, temp2 = temp2, temp3
print(temp3)

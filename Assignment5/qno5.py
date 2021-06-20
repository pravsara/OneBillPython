def numfor(func):
    def inner(num2, n):
        func(num2, n)
        for i in num2:
            print('+91', i[:5], i[5:])
    return inner
@numfor
def sr(num2, n):
    for i in range(0, n):
        if len(num2[i]) == 10:
            num2[i] = num2[i][:6]+num2[i][6:]
        elif len(num2[i]) == 11:
            num2[i] = num2[i][1:7]+num2[i][7:]
        else:
            num2[i] = num2[i][2:8]+num2[i][8:]
    num2.sort()
n = int(input('Enter the number of mobile numbers : '))
num1 = []
for i in range(0, n):
    num1.append(input('Enter mobile number : '))
sr(num1, n)

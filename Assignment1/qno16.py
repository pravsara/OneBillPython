from ast import literal_eval as lt
def printSum(dic):
    sum = 0
    for i in dic.values():
        sum += i
    return sum

dic = lt(input("Enter the values : "))
print("Sum = ", printSum(dic))
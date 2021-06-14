n = int(input("Enter the Value:"))
if n in range(1900,100000):
    if n % 4 == 0:
        print(True)
    else :
        print(False)
else :
    print('Invalid Input')
n = int(input("Enter the Value:"))
if n in range(1,101):
    if n%2 != 0:
        print('Weird')
    else :
        if n in range(2, 5):
            print(' Not Weird')
        elif n in range(6,11):
            print('Weird')
        elif n > 10:
            print('Not Weird')
else :
    print("Invalid Number")

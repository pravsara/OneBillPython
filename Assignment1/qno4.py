n = int(input("Enter limit : "))
a = ['']
if(n >= 2 and n <= 5):
    a = [int(x) for x in input('Enter Values : ').split()]
    a.sort(reverse=True)
    for i in range(0,n-2) :
        if(a[i] != a[i+1]) :
            print(a[i+1])
            break
else :
    print('Invalid Input')
n = int(input("Enter the Value:"))
if n in range (1,21):
    for x in range(0,n):
        print(x*x)
else:
    print("Invalid Number")

s = input("Enter the String : ")
if(0 <= len(s) and len(s) <= 1000):
    print("True" if s.isalnum() else "False")
    print(s.isalpha())
    print(s.isdigit())
    print(s.isupper())
    print(s.islower())
else :
    print('Invalid Input')
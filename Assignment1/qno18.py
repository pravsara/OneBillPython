s = input("Enter the String : ")
s = list(s)
d = {item: s.count(item) for item in s}
print(d)
s = input("Enter the string : ")
print("-------Using with Slice operator----------")
print("Reverse of the string: "+s[::-1])
print("-------Using without slice operator--------")

for i in range(len(s)-1, -1, -1):
    print(s[i], end="")
print()
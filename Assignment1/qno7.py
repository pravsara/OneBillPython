s = input("Enter the string : ")
index , value = (input("Enter the index and value to be updated : ").split(" "))
index = int(index)
t = s[0:index]+value+s[index+1:len(s)]
print(t)
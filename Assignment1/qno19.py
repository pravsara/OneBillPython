s = input("Enter the String : ")
s = list(s)
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
d = {item: s.count(item) for item in s if item in vowels}
print(d)
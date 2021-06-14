s = input("Enter the String : ")
vowels = 'AEIOUaeiou'
d = {item: s.count(item) for item in s if item in vowels}
print(d)
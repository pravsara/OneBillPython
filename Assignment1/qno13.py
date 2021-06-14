s = input("Enter the word : ")
s = list(s)
vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
print(list([x for x in s if x in vowels]))
s = set(s)
vowels = set(vowels)
print(s.intersection(vowels))
s = input('Enter String Value : ')
t = ''
for i in range(1, len(s), 2) :
    t = t + s[i]
for i in range(0, len(s), 2):
    t = t + s[i]
print(t)
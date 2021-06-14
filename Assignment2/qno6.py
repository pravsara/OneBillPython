s = input('Enter String Value : ')
print([i+" : "+str(s.count(i)) for i in s], sep=" ")
s = "eeaabbfksjfbbeelslss"
print(*[i+"-----"+str(s.count(i)) for i in s], sep=" ")
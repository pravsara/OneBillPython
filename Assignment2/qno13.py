s = "a4b3c2"
res = ""
for i in range(0, len(s)):
    if(s[i].isdigit()):
        res += s[i-1]*int(s[i])
print(res)
import random
import string
st = ''
l = [()]
for i in range(0,6):
    if i % 2 == 0:
        st += random.choice(string.ascii_letters)
    else:
        j = random.randrange(0,9,1)
        st += str(j)
print(st)
s = input('Enter String : ')
l = s.split(" ")
print(''.join([i[::-1]+" " for i in l]))
x = lambda a, b, c : a if a>b and a>c else b  if b>c else c
print(x(int(input('Enter first value : ')), int(input('Enter second value : ')), int(input('Enter third value : '))))
a, b = (int(x) for x in input('Enter Values: ').split())
print("a=b" if a == b else "a>b" if a > b else "(a<b)")

n = [int(x) for x in input('Enter Values : ').split()]
#without lambda
def fun(x):
    if x % 2 == 0:
        return x
m = filter(fun, n)
for y in m:
    print(y)
#with lambda
f = lambda a: a if a % 2 == 0 else 0
o = filter(f,n)
for p in o:
    print(p)
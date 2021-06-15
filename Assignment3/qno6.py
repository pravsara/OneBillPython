import functools
n = [int(x) for x in input('Enter values : ').split()]
print(functools.reduce(lambda a,b : a+b , n))
t = (int(x) for x in input("Enter : ").split(" "))
t = tuple(t)
print("Sum = "+str(sum(t)))
print("Average = "+str(sum(t)/len(t)))
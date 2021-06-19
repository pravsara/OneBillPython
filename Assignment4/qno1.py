def printfun(func):
    def inner(textinp, i):
        if i > 0:
            for j in range(0,i):
                print(textinp)
        else:
            func(textinp, i)
    return inner

@printfun
def pri(name, i):
    if i < 0:
        print('Enter positive number')

n = input('What do you want to print ? ')
o = input('How many times do you want to print the statement?')
pri(n, int(o))
# find greates number from three numbers using a function.
def greates(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c

a = 30
b = 5
c = 2

print(greates(a, b, c))
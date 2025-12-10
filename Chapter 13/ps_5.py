from functools import reduce
a = [1, 2, 4434, 232, 343, 223, 53, 65, 45, 55]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, a))

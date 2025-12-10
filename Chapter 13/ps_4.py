def divisible(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 2, 4434, 23232, 3434, 2323, 53, 65, 45, 55]

f = list(filter(divisible, a))
print(f)
# multiplication of number in n table using loop with revesred order
n = int(input("Enter number: "))

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}")
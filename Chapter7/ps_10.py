"""
For n = 3
    ***
    * *
    ***

"""

n = int(input("Enter number: "))
for i in range(1, n+1):
    #print(f"This is i value: {i}")
    if(i==1 or i==n):
        #print(f"inside if condition: {i}")
        print("*"* n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")
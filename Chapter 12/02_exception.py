try:
    a = int(input("Enter a number: "))
    print(a)

except ValueError as v:
    print(f"Value Error: {v}")
    
except Exception as e:
    print(e)


# Example: Print Hello, World!
print("Hello, World!")
# Example: Taking user input
# name = input("Enter your name: ")
# print(f"Hello, {name}!")

print("---------------------------")

# Example: Length of a string
text = "Hello, World!"
print(len(text))  # Output: 13

print("---------------------------")

# Example: Using range to create a list of numbers
for i in range(5):
    print(i)

print("---------------------------")


# Example: Summing a list of numbers
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  # Output: 15

print("---------------------------")

# Example: Finding the max and min values
numbers = [3, 1, 4, 1, 5, 9]
print(max(numbers))  # Output: 9
print(min(numbers))  # Output: 1

print("---------------------------")

# Example: Zipping two lists together
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]
zipped = list(zip(names, scores))
print(zipped)  # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 88)]

print("---------------------------")

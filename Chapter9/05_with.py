f = open("file.txt")
data = f.read()
f.close()


# the same can written using with statment like this:
with open("file.txt") as f:
    print(f.read())

# You dont need to add f.close() for close the file
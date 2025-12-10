# read the file and find the word is found or not from the file content.
f = open("poem.txt")
content = f.read()
if("twinkle" in content):
    print(" Word is found!!")
else:
    print("Word is not found!!")

f.close()
# write a python program to print a contents of directory using the os module. search online for the function which does that.

import os
directory_path = "/home/emb-alpesol/Downloads"

contents = os.listdir(directory_path)


for item in contents:
    print(item)

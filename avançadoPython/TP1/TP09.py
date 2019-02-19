import os

path = os.getcwd()
directory = os.listdir(os.getcwd())
for file in directory:
    print(file, os.path.getmtime(file))
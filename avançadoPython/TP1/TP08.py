import os

path = os.getcwd()
directory = os.listdir(os.getcwd())

test = path + '\\TP01.py'

print(test)

for file in directory:
    print(os.stat(file).st_size/1000, 'KB')
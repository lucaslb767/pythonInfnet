import os

p = os.path.abspath('C:/Users/Lucas/Downloads/python-3.7.2.exe')
print(p)
if os.path.isfile(p):
    print(p, 'é um arquivo!')
else:
    print(p, 'não é um arquivo!')
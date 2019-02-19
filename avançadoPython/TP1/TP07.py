import os

file = 'avançadoPython\TP01.py'
path = os.path.split(file)

print(os.path.abspath(path[0]))
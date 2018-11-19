import psutil

#obtem frequencia minima e maxima possivel
print(psutil.cpu_freq())

#obtem frequencia atual

print('frequencia atual em MHz:', psutil.cpu_freq().current)
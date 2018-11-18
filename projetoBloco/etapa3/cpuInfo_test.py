import cpuinfo

info = cpuinfo.get_cpu_info()

for i in info:
    print(i,":", info[i])


#para obter o numero de núcleos físicos de CPU:
import psutil

print('\nnucleos fisicos',psutil.cpu_count(logical=False))
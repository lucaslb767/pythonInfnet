import psutil
import time

mem = psutil.virtual_memory() #captura memoria total em bytes

print('memoria total',mem)

mem_gb = round(mem.total/(1024*1024*1024),2) #transforma em Gigabyte

print('memoria em GB',mem_gb)




print('pocentagem processador', psutil.cpu_percent()) #mostra quanto do processador está sendo utilizado



for i in range(0, 100):
    print(psutil.cpu_percent()) #esse loop faz aparecer a cada 1 segundo o quanto do processador está sendo utilizado
    time.sleep(1)






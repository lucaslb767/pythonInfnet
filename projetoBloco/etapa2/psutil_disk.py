import psutil

disk = psutil.disk_usage('.')

print(disk)

print('Total',disk.total,'B')
print('Em uso', disk.used, 'B')
print('Livre', disk.free,'B')

print('Total', round(disk.total/(1024*1024*1024), 2), 'GB')
print('Em uso', round(disk.used/(1024*1024*1024), 2), 'GB')
print('Livre', round(disk.free/(1024*1024*1024), 2), 'GB')

print('Percentual de disco usado:', disk.percent ,'%')
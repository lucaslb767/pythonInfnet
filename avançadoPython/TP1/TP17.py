import psutil
psutil.cpu_percent(percpu=True)
for i in range(20):
    print(psutil.cpu_percent(interval=1),"%")

#ok
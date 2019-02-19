import psutil, os

print("Nome do dispositivo:", os.getenv("SystemDrive"))
print("Formato: ", psutil.disk_partitions(os.getenv("SystemDrive"))[0][2])
print("Total: ", psutil.disk_usage(os.getenv("SystemDrive")).total/1024**3, "GB")
print("Disponível: ", psutil.disk_usage(os.getenv("SystemDrive")).free/1024**3, "GB")

#ok

import psutil, os
print("Espaço Livre:", psutil.disk_usage(os.getcwd()).free/1024**3, "GB")

#ok

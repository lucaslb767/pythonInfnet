import psutil

print("Memória Virtual: ", psutil.virtual_memory().total/1024**3, "GB")
print("Memória de Paginação: ", psutil.swap_memory().total/1024**3, "GB")

#ok
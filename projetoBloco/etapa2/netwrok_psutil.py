import psutil

dic_interfaces = psutil.net_if_addrs()

print(dic_interfaces)

print(dic_interfaces['Ethernet 2'][0].address)
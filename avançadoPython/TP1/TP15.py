import psutil, os
from datetime import datetime, time

def findProcessIdByName(processName):

    listOfProcessObjects = []

    #Iterate over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Check if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower():
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess):
           pass

    return listOfProcessObjects;

# Find PIDs od all the running instances of process that contains 'chrome' in it's name
listOfProcessIds = findProcessIdByName('chrome')

if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       print((processID ,processName))
else:
   print('No Running Process found with given text')

pid = 304
p = psutil.Process(pid)
if psutil.pid_exists(pid):
    print("a process with pid %d exists" % pid)
    print(p.username())
    print(datetime.fromtimestamp(p.create_time()))
    print(p.memory_info().rss*10**-3, "KB")
else:
    print("a process with pid %d does not exist" % pid)
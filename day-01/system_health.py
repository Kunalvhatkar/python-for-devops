import psutil
#use py -m pip install psutil / pip install psutil / pip3 install psutil
def check_threshold():
    sys_threshold = int(input("Enter threshold value in percent :"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("Current Cpu usage % :",current_cpu)

    if current_cpu > sys_threshold:
        print("Alert Email send..", current_cpu)
    else:
        print("Cpu in safe")
    
    current_memory = psutil.virtual_memory()
    print("Current memory usage in %", current_memory.percent)

    if current_memory.percent > sys_threshold:
        print("Alert Email send..", current_memory)
    else:
        print("memory in under use")

    current_disk = psutil.disk_usage('C:\\')
    print("current disk usage in %", current_disk.percent)

    if current_disk.percent > sys_threshold:
        print("Alert Email send..", current_disk)
    else:
        print("disk in under use")

#current_memory & current_disk returs an object (svmem) not in integer form
#we use (current_memory.percet & current_disk.percent) instead of (current_memory & current_disk ) in if statement
# Because it returns an object (svmem) containing multiple attributes, and .percent gives numeric usage value for comparison.

check_threshold()

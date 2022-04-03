import psutil
from plyer import notification
import time

from psutil import disk_partitions , cpu_count ,disk_usage , cpu_percent


logical_cpus = cpu_count()
cpu_usage = cpu_percent(interval=1 , percpu=True)
disk_used  = disk_usage(path="/")
disk_used_c  = disk_usage(path="C:/")
pricess = psutil.pids()
def disk():
    print("Logical Cpus in This machine are >> " + str(logical_cpus))
    x = disk_partitions(all)
    print("")
    print("Partition In Machine Are >> ")
    for y in x:
        print(y)  
    print("")
    print("Disk Usage In this drive Is As Follows >> " + str(disk_used))
    print("")
    print("Disk Usage In C Drive Is >> " + str(disk_used_c))
    print("")
    print("Cpu Usage Per Logical Cpu Is As Follows >>" )
    print("")
    print(cpu_usage)
    print("")
    for t in range(4) :
        cv = cpu_usage[t]
        print("CPU " + str(t) +  " USAGE IS " +str(cv) + " % ")
    print("")
    k = len(pricess)      
    print( "Number Of running Processes >> "+str(k))
    print("")
localtime = time.asctime( time.localtime(time.time()) )

battery = psutil.sensors_battery()



def check_power(now_now = localtime):
            if True:
                percent_remain = battery.percent
                notification.notify(
                    title = "Battery Percentage On " + str(now_now),
                    message = str(percent_remain) + "% To Spend",
                    
                )

        
check_power()


disk()
        
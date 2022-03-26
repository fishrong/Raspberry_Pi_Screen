import os


def get_ram_info():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:4])


def get_disk_space():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            return (line.split()[1:5])


def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return res.replace("temp=", "").replace("'C\n", "")


def get_cpu_use():
    return str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())

def get_ram_percent():
    ram_stats = get_ram_info()
    ram_total = round(int(ram_stats[0]) / 1000, 1)
    ram_used = round(int(ram_stats[1]) / 1000, 1)
    return ram_used / ram_total

def get_disk_space_percent():
    return get_disk_space()[3]
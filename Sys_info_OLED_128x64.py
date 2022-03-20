# -*- coding: utf-8 -*-
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from PIL import Image, ImageFont, ImageDraw
import time, datetime, os

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial, rotate=0) # Rotation setting

# Folder directory
basedir = os.path.dirname(os.path.realpath(__file__))  
fontdir = os.path.join(basedir, 'fonts')
tempdir = os.path.join(basedir, 'temp')

# Font setting
font = 'MYRIADPRO-REGULAR.OTF'
font_0 = ImageFont.truetype(os.path.join(fontdir, font), 28)
font_1 = ImageFont.truetype(os.path.join(fontdir, font), 18)
font_2 = ImageFont.truetype(os.path.join(fontdir, font), 12)

print('OLED 128*64 is using.')
print('*Press Ctrl + c to quit.*')

import gpiozero
def cpuTemp_info():
    n = round(gpiozero.CPUTemperature().temperature,1)
    n = str(n) + '°'
    return n

import psutil
def psutil_info():
    # Get cpu statistics
    cpu = str(psutil.cpu_percent()) + '%'

    # Calculate memory information
    memory = psutil.virtual_memory()
    # Convert Bytes to MB (Bytes -> KB -> MB)
    available = round(memory.available/1024.0/1024.0/1024.0,1)
    total = round(memory.total/1024.0/1024.0/1024.0,1)
    # mem_info = str(available) + 'GB free / ' + str(total) + 'GB total ( ' + str(memory.percent) + '% )'
    mem_info = str(memory.percent) + '%' 

    # Calculate disk information
    disk = psutil.disk_usage('/')
    # Convert Bytes to GB (Bytes -> KB -> MB -> GB)
    free = round(disk.free/1024.0/1024.0/1024.0,1)
    total = round(disk.total/1024.0/1024.0/1024.0,1)
    # disk_info = str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
    disk_info = str(disk.percent) + '%'

    return cpu, mem_info, disk_info

import netifaces
def ip_address():
    # print(netifaces.interfaces())
    # print(netifaces.ifaddresses('wlan0'))
    wlan0_ip = netifaces.ifaddresses('wlan0')[2][0]['addr']
    return wlan0_ip

try:
    while True:
        # strDate = time.strftime('%Y-%m-%d')
        strTime = time.strftime('%H:%M:%S')
        cpuTemp = cpuTemp_info()
        cpuUsage, memUsage, diskUsage = psutil_info()
        ipAddrs = ip_address()
        with canvas(device) as draw:
            # draw.text((0, 0), strDate, font=font_2, fill=255)
            draw.text((0, 0), strTime, font=font_1, fill=255)

            draw.text((0,26), 'MEM :  ' + memUsage, font=font_2, fill=255)
            draw.text((0,39), 'DISK  :  ' + diskUsage, font=font_2, fill=255)
            draw.text((0,55), ipAddrs, font=font_2, fill=255)

            draw.text((90, 0), 'CPU', font=font_2, fill=255)
            draw.text((80,20), cpuUsage, font=font_1, fill=255)
            draw.text((80,40), cpuTemp, font=font_1, fill=255)
        time.sleep(1)

except KeyboardInterrupt:
    print('leanup')
    exit()

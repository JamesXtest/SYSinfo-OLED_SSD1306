# SYSinfo-OLED_SSD1306
#### Display system information of Raspberry pi in the OLED screen.
![Imgur](https://i.imgur.com/Bf01p2d.jpg)

The below information will display in oled screen  
+ Time
+ Temperature & usage of CPU
+ Usage of Memory & SD card
+ Wlan IP address

#### Hardware requirements 
+ Raspberry pi with python 3.7 or above. (tested on pi zero & 4B)
+ OLED screen with chip in SSD1306 / SSD1309

#### Installation
+ Luma.OLED: Display drivers for SSD1306 / SSD1309    
https://luma-oled.readthedocs.io/en/latest/index.html  
https://luma-oled.readthedocs.io/en/latest/install.html

+ GPIO Zero  
https://gpiozero.readthedocs.io/en/stable/
> ```python3
> sudo pip3 install gpiozero
> ```

+ Psutil (process and system utilities)    
https://pypi.org/project/psutil/ 
> ```python3
> pip install psutil
> ```

+ Netifaces  
https://pypi.org/project/netifaces/  
> ```python3
> pip install netifaces
> ```

+ Fonts  
Recommend to add the below fonts to font folder,
> - MYRIADPRO-REGULAR.OTF

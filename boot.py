#############################################
#  CO2 Smoke Project - Sept 22 2022          #
#############################################
# This file is executed on every boot (including wake-boot from deepsleep)
# Removed webrepl to reduce overhead

from machine import Pin
pb14 = Pin(14, Pin.IN, Pin.PULL_UP)
pb15 = Pin(15, Pin.IN, Pin.PULL_UP)
pb27 = Pin(27, Pin.IN, Pin.PULL_UP)
pb32 = Pin(32, Pin.IN, Pin.PULL_UP)
pb33 = Pin(33, Pin.IN, Pin.PULL_UP)
pb25 = Pin(25, Pin.IN, Pin.PULL_UP)
pb34 = Pin(34, Pin.IN, Pin.PULL_UP)
pb39 = Pin(39, Pin.IN, Pin.PULL_UP)
print("Pins set to input")

'''
Notes to assist programming

rshell -p COM##

rm /pyboard/main.py
rm /pyboard/rtns.py
rm /pyboard/ntptimex.py

rsync -m \ota1 /pyboard

*********** Webportal Notes ****************
ls -l

cd /home/LogServer2

java -jar LogServer2.jar 9092

nohup java -jar LogServer2.jar 9092 &
'''

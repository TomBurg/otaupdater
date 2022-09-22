##################################
# Misc subroutines  May 4 2022   #
##################################
# 
# rtns.py by TAB

import sys
import time
import utime
import machine
from machine import RTC
from machine import Pin
import ubinascii
import network
from machine import Pin, I2C
from machine import Pin, PWM



smoke = False
carbmono = False

sta_if = network.WLAN(network.STA_IF)  # create station interface
sta_if.active(True)   # activate the interface

class SUBRTNSException(Exception):
    #print("rtns exception")
    pass

class SUBRTNSBW:

    def __init__(self,initclock):
        self.initclock = initclock
        i2c = I2C(1, scl=Pin(22), sda=Pin(23), freq=50000)
        self.p4  = Pin(4, Pin.IN, Pin.PULL_UP)
        self.p12 = Pin(12, Pin.OUT)
        self.p13 = Pin(13, Pin.OUT)  #Red LED
        self.p14 = Pin(14, Pin.IN, Pin.PULL_UP)
        self.p15 = Pin(15, Pin.IN, Pin.PULL_UP)
        self.p21 = Pin(21, Pin.IN, Pin.PULL_UP)
        self.p25 = Pin(25, Pin.IN, Pin.PULL_UP)
        self.p26 = Pin(26, Pin.IN, Pin.PULL_UP)
        self.p27 = Pin(27, Pin.IN, Pin.PULL_UP)
        self.p32 = Pin(32, Pin.IN, Pin.PULL_UP)
        self.p33 = Pin(33, Pin.IN, Pin.PULL_UP)
        self.p34 = Pin(34, Pin.IN, Pin.PULL_UP)
        self.p39 = Pin(39, Pin.IN, Pin.PULL_UP)
        self.blinkRed(0.25)

    def ButtonA(self):
        return(self.p15.value())

    def ButtonB(self):
        return(self.p32.value())

    def ButtonC(self):
        return(self.p14.value())

    def Test4(self):
        return(self.p4.value())

    def Test14(self):
        return(self.p14.value())
    
    def Test15(self):
        return(self.p15.value())

    def Test21(self):
        return(self.p21.value())
    
    def Test26(self):
        return(self.p26.value())

    def Test27(self):
        return(self.p27.value())

    def Test32(self):
        return(self.p32.value())

    def Test33(self):
        return(self.p33.value())

    def Test25(self):
        return(self.p25.value())

    def Test34(self):
        return(self.p34.value())

    def Test39(self):
        return(self.p39.value())
    
    def blinkRed(self,btime):
        self.p13.on()
        time.sleep(btime)
        self.p13.off()
        time.sleep(btime)

    def Redon(self):
        self.p13.on()

    def Redoff(self):
        self.p13.off()

    def blink_cnt(self,count):
        print (" Blinks ", end="")
        for n in range(0, count):
            self.blinkRed(0.1)
            time.sleep(0.1)
            print (n," ", end="")
        #print(count, " Blinks done\n\r")

    def get_id(self):
        Muid = ubinascii.hexlify(machine.unique_id())
        UID = str(Muid.decode('utf-8'))
        GUID = UID[8:12]
        return GUID.upper()
    
    def enter_truck_id(self):
        loop = True
        combineid = ''
        while(loop):
            print('Enter Branch ID - 3 Characters')
            branchid = self.readusb(3)
            print('Branch ID =', branchid)
            print('Enter Truck number - 3 digits')
            trucknum = self.readusb(3)
            print('trucknum =',trucknum)
            if(int(trucknum) > 999):
                print('truck number error')
            TruckID = str(branchid[0:3]) + str(trucknum[0:3])
            #print('TruckID ->',TruckID)
            print('Enter y - or else repeat')
            saveid = sys.stdin.read(1)
            print('confirm = ', saveid )
            if(saveid[0] == 'y'):
                print('TruckID ==> ', TruckID)
                loop = False
        return(TruckID)

    def enter_cali(self,digits):
        loop = True
        #combineid = ''
        while(loop):
            calfactor = self.readusb(digits)
            print('Save to memory? - Enter y')
            saveid = sys.stdin.read(1)
            print('confirm = ', saveid )
            if(saveid[0] == 'y'):
                print('Saving -> ', calfactor)
                loop = False
        return(calfactor)

    def enter_califactor(self,digits):
        calfactor1 = 0.0
        readstring = self.readusb(digits)
        calistring = readstring[0:5]
        print('readstring[0:4] ', readstring[0:5])
        calfactor1 = round(float(calistring),3)
        print('calfactor1 = ', calfactor1)
        return(calfactor1)
    
    def readusb(self,totald):
        line = ''
        for n in range(0 , totald):
            newchar = sys.stdin.read(1)
            newchar.rstrip()
            print (newchar, end="")
            line = line + newchar
        #print('readusb = ', line)
        return(line)

    def wifitimeout(self, wttime):
        wificnttime = 0
        while not sta_if.isconnected():
            wificnttime += 1
            #machine.idle() # save power while waiting
            print("*",wificnttime,end='')
            self.blinkRed(0.25)
            #time.sleep_ms(250)
            if wificnttime > wttime:
                print('wifitimeout -- reboot')
                machine.reset()
                #break       

    def connectwifi(self,confirmwifi):
        if ((not sta_if.isconnected()) & confirmwifi):
            sta_if.active(True)   # activate the interface
            time.sleep(0.5)
            nets = sta_if.scan()  # scan for access pointsrm /pyboard
            #print('Nets:  ', nets)
            wifilink = 'Not Found'
            i=0
            for net in nets:
                if sta_if.isconnected():
                    print('Already connected - break here \n\r')
                    break
                if (net[0].find(b'PS_Hotspot') == 0):
                    print('PS_Hotspot found!')
                    sta_if.connect(ssidpshot_ , wp2pshot_pass )
                    self.wifitimeout(40)
                    #while not sta_if.isconnected():
                        #machine.idle() # save power while waiting
                        #print(".",end='')
                        #time.sleep_ms(250)
                    print('PS_Hotspot connection succeeded!')
                    wifilink = 'PS_Hotspot'
                    break

            for net in nets:
                if sta_if.isconnected():
                    print('Already connected - break here \n\r')
                    break
                if (net[0].find(b'Proshred_Private') == 0):
                    print('Proshred_Private')
                    sta_if.connect(ssidproshred_ , ssidproshred_pass )
                    self.wifitimeout(40)
                    #while not sta_if.isconnected():
                    #    #machine.idle() # save power while waiting
                    #    print(">",end='')
                    #    time.sleep_ms(250)
                    print('Proshred_Private connection succeeded!')
                    wifilink = 'Proshred_Private'
                    break

            for net in nets:
                if sta_if.isconnected():
                    print('Already connected - break here \n\r')
                    break
                if (net[0].find(b'Roboburghot') == 0):
                    print('Roboburghot Network found!')
                    sta_if.connect(ssidhot_ , wp2hot_pass )
                    self.wifitimeout(40)
                    print('Roboburghot connection succeeded!')
                    wifilink = 'Roboburghot'
                    break
            i=0
            for net in nets:
                if sta_if.isconnected():
                    print('Already connected - break here \n\r')
                    break
                if (net[0].find(b'Roboburg') == 0):
                    print('Roboburg Network found!')
                    sta_if.connect(ssid_ , wp2_pass )
                    while not sta_if.isconnected():
                        #machine.idle() # save power while waiting
                        print(".",end='')
                        time.sleep_ms(250)
                    print('Roboburg connection succeeded!')
                    wifilink = 'Roboburg'
                    break
                else:
                    print("* Not Connected to WiFi - wait 3 - try again * \n")
                    time.sleep(3)
                    i += 1
                    nets = sta_if.scan()
                    print('Nets attempt: ', i, '\n\r', nets)
            return(wifilink)

    def disconnectwifi(self):
        if (sta_if.isconnected()):
            sta_if.disconnect()
            sta_if.active(False)   # deactivate the interface
            sta_if = None
            print("Disconnected from WiFi")
            self.blink_cnt(5)
        else:
            print("Wasn't Connected")

'''
End of rtns.py routines

rm /pyboard/main.py
rsync -m \smokeco4 /pyboard
'''

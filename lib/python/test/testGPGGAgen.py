#!coding:utf-8

import pynmea2
import sys
import re

def checksum(data):
    res = 0
    data = data.split('$')[1]
    for c in data:
        res ^= ord(c)

    return hex(res)
if __name__ == '__main__':
    gpgga = '$GPGGA,102154.552,4308.0718,N,14114.9862,E,1,03,19.8,48.4,M,29.5,M,,0000'
    
    altdata = 100
    time = 101114
    for i , alt in enumerate(range(0 , altdata, 5)):
        #print(pynmea2.GGA('GP' + 'GGA' + str(time+i),'4308.0718' + 'N' + '14114.9862' + 'E' + '' + '01' + '03' + '19.8' + '48.4' + 'M' + str(29.5+alt) + 'M' + '' + '0000'))
        data = '$GPGGA,' + str(time+i) + ',4308.0718' + ',N' + ',14114.9862' + ',E' + ',' + ',01' + ',03' + ',19.8' + ',48.4' + ',M,' + str(29.5+alt) + ',M' + ',' + ',0000'
        data += '*'+str(checksum(data)).split('x')[1]
        print(data)

    for i , alt in enumerate(range(altdata, 0, -5)):
        data = '$GPGGA,' + str(20+time+i) + ',4308.0718' + ',N' + ',14114.9862' + ',E' + ',' + ',01' + ',03' + ',19.8' + ',48.4' + ',M,' + str(alt-29.5) + ',M' + ',' + ',0000'
        data += '*'+str(checksum(data)).split('x')[1]
        print(data)


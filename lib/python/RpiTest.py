#!coding:utf-8


class GPIO:
    BCM = ''
    HIGH = 'HIGH'
    LOW = 'LOW'
    OUT = 'OUT'

    def setmode(bcm):
        pass

    def setup(ionum, INOUT):
        print(str(ionum)+","+str(INOUT))

    def output(ionum, state):
        print(str(ionum)+","+str(state))

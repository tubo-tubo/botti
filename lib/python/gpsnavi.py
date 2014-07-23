#!coding:utf-8


class gpsparser(object):
    import serial
    import math
    import pynmea2
    from pyproj import Geod

    def __init__(self, portname=None, goal=[138.75665666666666, 35.68582166666667]):
        self.goal = goal
        if portname is not None:
            self.ser = self.serial.Serial(port=portname)

    def gpsupdate(self, debuggpsvalue=None):
        if debuggpsvalue is None:
            readline = self.ser.readline()
            self.gpsdata = self.NMEAanAlysis(readline)
        else:
            self.gpsdata = self.NMEAanAlysis(debuggpsvalue)

    def NMEAanAlysis(self, data):
        return self.pynmea2.parse(data)

    def timestamp(self):
        return self.gpsdata.timestamp

    def lat(self):
        return float(self.gpsdata.lat)

    def latitude(self):
        return float(self.gpsdata.latitude)

    def lon(self):
        return float(self.gpsdata.lon)

    def longitude(self):
        return float(self.gpsdata.longitude)

    def sat_receivejudge(self):
        if int(self.gpsdata.num_sats) >= 4:
            return True
        else:
            return False

    def altitude(self):
        return float(self.gpsdata.altitude)

    def goalcalc(self):
        nowpos = [self.longitude(), self.latitude()]
        g = self.Geod(ellps='WGS84')
        self.goalaz, self.goalbackaz, self.goaldist = g.inv(nowpos[0], nowpos[1],self.goal[0], self.goal[1])

    def goaldistance(self):
        return self.goaldist

    def goalhorizontaldistance(self):
        return self.math.cos(self.goalazimath())*self.goaldistance()

    def goalverticaldistance(self):
        return self.math.sin(self.goalazimath())*self.goaldistance()

    def goalazimath(self):
        return float(self.goalaz)

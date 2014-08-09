import gpsnavi
import unittest
import datetime
import mox3
import go_f
import os


class Testgpsnavi(unittest.TestCase):
    #lon = 139.649867
    lon = 141.24322166666667
    lat = 43.123041666666666
    #lat = 35.705385
    goal = [[lon, lat]]
    gps = gpsnavi.gpsparser(goal=goal)
    #getdis = go_f.getdistance()

    def test_readgps(self):
        self.gps.gpsupdate(debuggpsvalue='$GPGGA,035653.00,4307.5613,N,14114.6470,E,1,00,0.0,-0.2,M,0.0,M,,*70')
        self.assertEqual(self.gps.lat(), 4307.5613)
        self.assertEqual(self.gps.lon(), 14114.647)
        self.assertEqual(self.gps.latitude(), 43.12602166666667)
        self.assertEqual(self.gps.longitude(), 141.24411666666666)
        self.assertEqual(self.gps.timestamp(), datetime.time(3, 56, 53))
        self.assertEqual(self.gps.sat_receivejudge(), False)
        print(self.gps.sat_receivejudge())
        self.assertEqual(self.gps.altitude(), -0.2)
        self.gps.goalcalc()
        self.assertEqual(self.gps.goaldistance(), 338.98014818398985)
        self.assertEqual(self.gps.goalazimath(),-167.59266836658236)
        self.assertEqual(self.gps.goalverticaldistance(), 300.2753247263464)
        self.assertEqual(self.gps.goalhorizontaldistance(), -157.2967584641429)
        #print(self.gps.goalazimath())

    def test_readgpsserial(self):
        import serial
        import io
        import sys
        ser = serial.serial_for_url('loop://', timeout=1)
        sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
        f = ''
        if len(sys.argv) > 1:
            f = open(sys.argv[1])
        else:
            f = open(os.path.dirname(__file__)+'/test/teine.txt')
        for data in f.readlines():
        #    sio.write(data)
        #    sio.flush()
        #    self.gps.gpsupdate(debuggpsvalue=sio.readline())
            self.gps.gpsupdate(debuggpsvalue=data)
            print(self.gps.latitude())
            print(self.gps.longitude())
            self.gps.goalcalc()
            print("goal distance:"+str(self.gps.goaldistance()))
            print("goal azimath:"+str(self.gps.goalazimath()))
            print("goal vertical distance:"+str(self.gps.goalverticaldistance()))
            print("goal horizontal distance:"+str(self.gps.goalhorizontaldistance()))
        f.close()

    def test_getdistance(self):
        pass
        #self.getdis.goal = [37.0, 139.0]
        #self.assertEqual(self.getdis.goal, [37.0, 139.0])

if __name__ == '__main__':
    unittest.main()

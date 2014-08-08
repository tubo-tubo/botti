#!coding:utf-8

import go_GPIO
import numpy
import time

gps = gpsnavi.gpsparser(goal=goal)
groundlat = gps.altitude()	#現地で計測する予定
altave = []
passer = []

if gps.altitude >= groundlat + 50:
	passer.append("high")

while gps.altitude() <= groundlat + 30 and passer[0] = "high" :
	time.sleep(0.5)
	altave.append(gps.altitude())

	if groundlat - 10 <= numpy.average(altave) <= groundlat + 10 :
		time.sleep(30)
		go_GPIO.forward(20)

		lon = 141.24322166666667
		lat = 43.123041666666666
		lon1 = 139.649867
		lat1 = 35.705385
		#lon2 =
		#lat2 =
		goal = [[lon,lat]]
		check = [[lon1,lat1]]
		goal.extend(check)

		go_GPIO.GPIO.turn()
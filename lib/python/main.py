#!coding:utf-8

import go_GPIO

lon1 =
lat1 =
lon2 =
lat2 =
lon3 =
lat3 =

go_f.getdistance._goal = [[lon1,lat1]]
checkpoint = [[lon2,lat2],[lon3,lat3]]
go_f.getdistance._goal.extend(checkpoint)
go_GPIO.GPIO.turn()
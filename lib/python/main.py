#!coding:utf-8

import go_GPIO
import time
import gpsnavi


def landing(gps, groundalt):
    count = 0
    while True:
        gps.gpsupdate()
        if count >= 3:
            break
        if gps.altitude() >= groundalt + 50:
            count += 1

    count = 0
    while True:
        gps.gpsupdate()
        if count >= 10:
            break
        if groundalt - 10 <= gps.altitude() <= groundalt + 10:
            count += 1
    time.sleep(30)
    go_GPIO.forward(20)


def travel():
    go_GPIO.GPIO.turn()


def arrive():
    pass

if __name__ == '__main__':
    goal = []
    goal.append([141.24322166666667, 43.123041666666666])
    goal.append([139.649867, 35.705385])

    gps = gpsnavi.gpsparser(goal=goal)
    gps.gpsupdate()
    groundalt = gps.altitude()  # 現地で計測する予定
    landing(gps, groundalt)
    travel()
    arrive()

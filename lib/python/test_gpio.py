#!coding:utf-8

import RPi.GPIO as IO
import time

IO.setmode(IO.BCM)
IO.setup(18, IO.OUT)

IO.output(18, IO.HIGH)
time.sleep(1)
IO.output(18, IO.LOW)
time.sleep(1)


import RPi.GPIO as IO
import time
import sys

p3 = 22 # pin 15 右前
p4 = 23 # pin 16 右後ろ

p5 = 24 # pin 18 左前
p6 = 25 # pin 22 左後ろ
i  = sys.argv[0]

IO.setmode(IO.BCM)

IO.setup(p3,IO.OUT)
IO.setup(p4,IO.OUT)
IO.setup(p5,IO.OUT)
IO.setup(p6,IO.OUT)

while true:
	if i == 0:
		IO.output(p3,IO.HIGH)
		IO.output(p4,IO.HIGH)
		IO.output(p5,IO.LOW)
		IO.output(p6,IO.LOW)
	elif i == 1:
		IO.output(p3,IO.LOW)
		IO.output(p4,IO.LOW)
		IO.output(p5,IO.HIGH)
		IO.output(p6,IO.HIGH)
	elif i == 2:
		IO.output(p3,IO.LOW)
		IO.output(p4,IO.HIGH)
		IO.output(p5,IO.HIGH)
		IO.output(p6,IO.LOW)
	elif i == 3:
		IO.output(p3,IO.HIGH)
		IO.output(p4,IO.LOW)
		IO.output(p5,IO.LOW)
		IO.output(p6,IO.HIGH)
	else:
		IO.output(p3,IO.LOW)
		IO.output(p4,IO.LOW)
		IO.output(p5,IO.LOW)
		IO.output(p6,IO.LOW)

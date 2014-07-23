
import RPi.GPIO as IO
import time

p3 = 17  # pin 15 右前
p4 = 18  # pin 16 右後ろ

p5 = 22  # pin 18 左前
p6 = 27  # pin 22 左後ろ

IO.setmode(IO.BCM)

IO.setup(p3, IO.OUT)
IO.setup(p4, IO.OUT)
IO.setup(p5, IO.OUT)
IO.setup(p6, IO.OUT)

while True:
    print('[0,1,2,3,other_number]')
    i = int(raw_input().split()[0])
    time.sleep(1)
    if i == 0:
        IO.output(p3, IO.HIGH)
        IO.output(p4, IO.HIGH)
        IO.output(p5, IO.LOW)
        IO.output(p6, IO.LOW)
    elif i == 1:
        IO.output(p3, IO.LOW)
        IO.output(p4, IO.LOW)
        IO.output(p5, IO.HIGH)
        IO.output(p6, IO.HIGH)
    elif i == 2:
        IO.output(p3, IO.LOW)
        IO.output(p4, IO.HIGH)
        IO.output(p5, IO.HIGH)
        IO.output(p6, IO.LOW)
    elif i == 3:
        IO.output(p3, IO.HIGH)
        IO.output(p4, IO.LOW)
        IO.output(p5, IO.LOW)
        IO.output(p6, IO.HIGH)
    else:
        IO.output(p3, IO.LOW)
        IO.output(p4, IO.LOW)
        IO.output(p5, IO.LOW)
        IO.output(p6, IO.LOW)

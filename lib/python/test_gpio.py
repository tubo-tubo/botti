
import RPi.GPIO as io
import time

io.setmode(io.RMC)
io.setup(18,io.OUT)

io.output(18,io.HIGH)
time.sleep(1)
io.output(18,io.LOW)
time.sleep(1)


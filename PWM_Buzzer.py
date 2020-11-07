#-*- coding: utf-i -*-

import RPi.GPIO as GPIPO
import time

GPIPO.setwarnings(False)
GPIPO.setmode(GPIPO.BCM)

GPIPO.setup(18, GPIPO.OUT)
p = GPIPO.PWM(18, 100)

Frq = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5

p.start(10)

try:
    while 1:
        for fr in Frq:
            p.ChangeFrequency(fr)
            time.sleep(speed)
except KeyboardInterrupt:
    pass

p.stop()
GPIPO.cleanup()
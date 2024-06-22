from machine import Pin, PWM
from hcsr04 import HCSR04 
us = HCSR04(2,15)
Rgb = PWM(Pin(13))
rGb = PWM(Pin(12))
while True:
    Cv = int(us.distance_cm() * 255/404)
    Cr = 255 - Cv
    Rgb.duty(Cr*int(1023/255))
    rGb.duty(Cv*int(1023/255))
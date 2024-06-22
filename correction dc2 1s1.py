from machine import Pin, PWM
from hcsr04 import HCSR04 
Rgb = PWM(Pin(13))
rGb = PWM(Pin(12))
us = HCSR04(26,27)
def light_my_rgb(r,g):
    Rgb.duty(int(r*1023/255))
    rGb.duty(int(g*1023/255))
while True:
    Cv = int(us.distance_cm()*255/404)
    Cr = 255 - Cv
    # Cr = int((404-us.distance_cm())*255/404)
    light_my_rgb(Cr,Cv)
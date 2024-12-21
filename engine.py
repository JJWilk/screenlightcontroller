from colorgrab import *
from lightchanger import *
from constants import *
import time

# every x second, sample and change the light color based on the screen
on = True
while on:
    color = get_color()
    color = color.tolist()
    color.append(0)
    light_color = tuple(int(x) for x in color)
    changeLightColor(light_color)

    time.sleep(SECONDS_TO_WAIT)

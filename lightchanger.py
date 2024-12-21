import time
from constants import *
from pywizlight import wizlight, PilotBuilder
import asyncio

async def lightOn(lightIP, pilotBuilder):
    light = wizlight(lightIP)
    await light.turn_on(pilotBuilder)

async def lightOff(lightIP):
    light = wizlight(lightIP)
    await light.turn_off()

async def lightColor(rgbw):
    pilot = PilotBuilder(rgbw=rgbw, brightness=BRIGHTNESS)

    await lightOn(TOPLIGHT["IP"], pilot)
    await lightOn(BOTLIGHT["IP"], pilot)

def changeLightColor(rgbw):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(lightColor(rgbw))



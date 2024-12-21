# Screen/Light Controller

This project was intended as a personal project in order to sync my computer screen with my wifi controlled lights. The intend use-case is for watching movies, for a more cinematic experience. This uses Wiz brand lights, and is primarily based on the pywizlight package. 

I have two lights, but this could be extended to any number of lights with some minor code changes. 

### Using this project
If you want to use this code, you will have to get the ip/mac addresses of your lights and substitute that in constants. If using any number of lights other than 2, you'll also have to add/remove a line in lightChanger.lightColor(). 

Extra Packages needed (since this is a personal project, I did not add a requirements.txt)

    pip install pywizlight
    pip install opencv-python

### How it works
Every few seconds, this script will screenshot your screen. It will sample x number of pixels and average the color of those pixels, then send that color (through UDP) to the wiz lights. 

### Constants
Some constants to be aware of:

NUM_SAMPLES      -the number of pixels to sample. A higher number will be more computationally intense, but have a more consistant and accurate average color.

SECONDS_TO_WAIT   -this determines how often the lights change. Each iteration (capturing screenshot and changing the lights) takes around 100 milliseconds to change on their own, so thats the lower bound. Higher wait times can feel less responsive, but lower wait times might mean that your lights pulse a bit if your screen is changing constantly and also means the script is constantly taking screenshots and sending messages. Around .5 works fairly well. 

BRIGHTNESS    -this is the default brightness for the lights, from 0-255. For watching movies around 50-100 is reccomended. 

### Further Changes
- Will probably add dynamic brightness changes based on color
- May try to speed up response time, currently colorgrab.py line 9: img = ImageGrab.grab() is the slowest overall operation other than sending messages to wizlight, so potentially improving this may help.
- May add options for multiple colors (ie the top light is based on the top half of the screen)



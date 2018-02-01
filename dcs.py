# MIT License
#
# Copyright (c) 2018 Matt Jadud <matt@jadud.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from adafruit_circuitplayground.express import cpx
import time
# import board

ON          = True
OFF         = False
BUTTONA     = 0
BUTTONB     = 1
BUTTONAB    = 2

XAXIS       = 0
YAXIS       = 1
ZAXIS       = 2

RED         = 0
GREEN       = 1
BLUE        = 2
YELLOW      = 3
BLUEGREEN   = 4
PURPLE      = 5


def pause (ms):
    time.sleep(ms / 1000.0)

def setBrightness (brightness = 10):
    cpx.pixels.brightness = (brightness / 100.0)

def setupPixels (brightness = 10):
    setBrightness(brightness)
    cpx.pixels.fill((0,0,0))
    cpx.pixels.show()

def setAllPixelsTo (color = RED):
    if color == RED:
        setAllPixelsToRGB(255, 0, 0)
    elif color == GREEN:
        setAllPixelsToRGB(0, 255, 0)
    elif color == BLUE:
        setAllPixelsToRGB(0, 0, 255)
        
def setAllPixelsToRGB (red = 0, green = 0, blue = 0):
    for i in range(10):
        cpx.pixels[i] = (red, green, blue)

def setPixelRGB (ndx = 0, red = 0, green = 0, blue = 0):
    cpx.pixels[ndx] = (red, green, blue)
    
def getPixelRGB (ndx = 0, color = None):
    if color:
        return cpx.pixels[ndx][color]
    else:
        return cpx.pixels[ndx][color]

def colorWheel (pos):
	if pos < 85:
		return (pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return (255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return (0, pos * 3, 255 - pos * 3)
        
def graph (value, max):
    if (value < max):
        percent = (float(value) / max)
        max_ndx = int(10 * percent)
        for i in range(0, max_ndx):
            cpx.pixels[i] = color_wheel(int((i / 10.0) * 255.0))
    else:
        for i in range(0, 10):
            cpx.pixels[i] = color_wheel(int((i / 10.0) * 255.0))


def setupSingleTap ():
    cpx.detect_taps = 1
def setupDoubleTab ():
    cpx.detect_taps = 2

def wasTapped ():
    return cpx.tapped

# CONTRACT
# accel : int -> float
# PURPOSE
# Returns a floating point value for the acceleration in the 
# dimension given. Ranges from -9.8 to 9.8
# I lied. It gets big. > 50 when shaken. Just using it as a 
# tilt sensor, it ranges from -9.8 to 9.8... 
def getAccel (DIM = XAXIS):
    return cpx.acceleration[DIM]

def turnRedLED(onoroff):
    cpx.red_led = onoroff

def isTouched(pin):
    touches = [cpx.touch_A1, cpx.touch_A2, cpx.touch_A3, cpx.touch_A4, 
                cpx.touch_A5, cpx.touch_A6, cpx.touch_A7 ]
    return touches[pin - 1]

def getLux ():
    return cpx.light

def getTemperatureC ():
    return cpx.temperature

def startTone (tone = 256):
    cpx.start_tone(tone)

def stopTone ():
    cpx.stop_tone()

def isPressed(button = BUTTONA):
    if (button == BUTTONA):
        return cpx.button_a
    else:
        return cpx.button_b

class DebouncedButton(object):
    def __init__ (self, button):
        self.last_pressed = 0
        self.was_pressed  = False
        self.button       = button
        self.debounce     = 0.25
    
    def check (self):
        now = time.monotonic()
        if is_pressed(self.button) and (now - self.last_pressed) > self.debounce:
            self.last_pressed = now
            self.was_pressed = True
    def reset (self):
        self.was_pressed = False
    def state (self):
        return self.was_pressed
    def set_debounce (self, ms):
        self.debounce = (ms / 1000.0)

DA = DebouncedButton(BUTTONA)
DB = DebouncedButton(BUTTONB)

def watchButtons ():
    global DA, DB
    DA.check()
    DB.check()

def wasPressed (button = BUTTONAB):
    global DA, DB
    if (button == BUTTONAB) and (DA.state() or DB.state()):
        DA.reset()
        DB.reset()
        return True
    if (button == BUTTONA) and DA.state():
        DA.reset()
        return True
    if (button == BUTTONB) and DB.state():
        DB.reset()
        return True

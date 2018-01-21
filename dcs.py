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

def set_brightness (brightness = 10):
    cpx.pixels.brightness = (brightness / 100.0)

def setup_pixels (brightness = 10):
    set_brightness(brightness)
    cpx.pixels.fill((0,0,0))
    cpx.pixels.show()

def set_all_pixels_to (red = 0, green = 0, blue = 0):
    for i in range(10):
        cpx.pixels[i] = (red, green, blue)

def setup_single_tap ():
    cpx.detect_taps = 1
def setup_double_tap ():
    cpx.detect_taps = 2

def was_tapped ():
    return cpx.tapped

def red_led(onoroff):
    cpx.red_led = onoroff

def touch_on(pin):
    touches = [cpx.touch_A1, cpx.touch_A2, cpx.touch_A3, cpx.touch_A4, 
                cpx.touch_A5, cpx.touch_A6, cpx.touch_A7 ]
    return touches[pin - 1]

def get_lux ():
    return cpx.light

def get_temperature ():
    return cpx.temperature

def play_tone (tone = 256):
    cpx.start_tone(tone)

def stop_tone ():
    cpx.stop_tone()

def is_pressed(button = BUTTONA):
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

def watch_buttons ():
    global DA, DB
    DA.check()
    DB.check()

def was_pressed (button = BUTTONAB):
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
from dcs import *

setup_pixels(brightness = 1)
# detect_taps()

toggle = True

while True:
    watch_buttons()
    if was_pressed(BUTTONA):
        red_led(toggle)
        toggle = not toggle
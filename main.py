from dcs import *

setup_pixels(brightness = 1)
# detect_taps()

toggle = True

count = 0 
while True:
    watch_buttons()

    if was_pressed(BUTTONA):
        red_led(toggle)
        toggle = not toggle
        count += 1
        graph(count, 100)
        
    if was_pressed(BUTTONB):
        color = get_pixel(1, RED)
        if color == 255:
            set_pixel(1, 0, 255, 0)
        else:
            set_pixel(1, 255, 0, 0)
    
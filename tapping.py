    toggle = not toggle
    if was_tapped():
        set_all_pixels_to(255, 0, 0)
        time.sleep(1)
    if touch_on(A1):
        set_all_pixels_to(0, 255, 0)
        time.sleep(1)
    if get_lux() < 2:
        set_all_pixels_to(0, 0, 255)
        time.sleep(1)
    time.sleep(0.5)
    
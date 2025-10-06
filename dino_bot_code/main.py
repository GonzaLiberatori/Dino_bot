from detector import get_game_frame, detect_obstacle
from controller import jump
from config import loop_delay, scan_x_start, scan_y_start, scan_width, scan_height
import numpy as np
import time
import pygetwindow as gw

jump_cooldown = 0.1     # min time between jumps
last_jump = 0

print("Initialized bot, open chrome with the game and leave it visible")

time.sleep(3) #3 seconds pause

import pygetwindow as gw

# Search window Chrome
windows = gw.getWindowsWithTitle("Chrome")
if windows:
    w = windows[0]
    # Mover la ventana a (0, 0)
    w.moveTo(0, 0)
    print("Window moved to position (0, 0)")


#infinite loop
 
while True:
    result = get_game_frame()
    if result is None:   
        continue
    frame,left,top = result


    relative_x = scan_x_start - left
    relative_y = scan_y_start - top

    if detect_obstacle(frame, relative_x, relative_y):
        current_time = time.time()
        if current_time - last_jump > jump_cooldown:  
            jump()
            last_jump = current_time

time.sleep(loop_delay)   

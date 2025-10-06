import numpy as np
import cv2
import mss
import pygetwindow as gw
from config import scan_x_start, scan_y_start, scan_width, scan_height, obstacle_limit


#search chrome windows and return
def get_chrome_window():
    windows = gw.getWindowsWithTitle("Chrome")
    if windows:
        w = windows[0]
        return w.left, w.top, w.width, w.height
    return None

def get_game_frame():
    window_screen = get_chrome_window()
    if window_screen is None:
        print("❌ No window found")
        return None

    left, top, width, height = window_screen #desempaquetado de la tupla
    monitor = {"top": top, "left": left, "width": width, "height": height} #Need a dictionary with the screen coordinates

    #convert the screen in matrix with np.array
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(monitor))

    #converts the image to grayscale
    gray = cv2.cvtColor(screenshot,cv2.COLOR_BGR2GRAY)
    return gray, left, top

#retornamos left y top para sacar el verdadero valor de ventana scan_x_start - left - top

def detect_obstacle(frame, relative_x, relative_y):
#roi = region of interest "the box" in front of the dino where the bot goes to look for obstacles
    roi = frame[relative_y:relative_y + scan_height,
                 relative_x:relative_x + scan_width]
#star_row:end_row/star_column:end_column.
#the box is draw in front of the dino

    #show roi for debug
    cv2.imshow("ROI", roi)
    cv2.waitKey(1)

    # threshold for detecting dark pixels
    _,thresh = cv2.threshold(roi, 100, 255, cv2.THRESH_BINARY_INV)
    pixel_count = cv2.countNonZero(thresh)    #count pixels whites

    print(f"Pixel count (obstacle): {pixel_count}")

    if pixel_count > 30:  
        return True
    return False



import pyautogui
import time
from get_window import GameWindow, minimap_x, minimap_y 

iml = pyautogui.screenshot(region=(minimap_x, minimap_y, minimap_x + 170, minimap_y + 165))
iml.save

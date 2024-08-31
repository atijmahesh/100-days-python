from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import ImageGrab
import pyautogui

# pyautogui.displayMousePosition()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://elgoog.im/dinosaur-game/")

time.sleep(2)

stop_time = time.time() + 300  # Play for 5 minutes

# Function to detect obstacles and press space
def detect_obstacle():
    box = (200, 600, 250, 650) 
    image = ImageGrab.grab(bbox=box)                    
    gray_image = image.convert('L')          
    pixels = gray_image.load()         
   
    for x in range(gray_image.width):
        for y in range(gray_image.height):      
            if pixels[x, y] < 100:  
                return True  #
    
    return False

pyautogui.press('space')     
while True:
    if time.time() > stop_time:
        break
    if detect_obstacle():       
        pyautogui.press('space')    
  
driver.quit()       
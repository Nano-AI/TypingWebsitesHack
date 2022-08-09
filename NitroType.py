from multiprocessing.dummy import freeze_support
import time

import keyboard as kb
from pynput.keyboard import Controller
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc

if __name__ == "__main__":
    driver = uc.Chrome()
    driver.get('https://www.nitrotype.com/race')
    while True:
        input("Hit enter to get ready")
        driver.get('https://www.nitrotype.com/race')
        input("Hit enter once page is loaded")
        words = driver.find_elements_by_css_selector('span.dash-word')
        print(f"Press enter to start")
        time.sleep(1)
        typeKey = Controller()
        while not kb.is_pressed('enter'):
            time.sleep(0.01)
        for word in words:
            print(word.text)
            for character in word.text:
                typeKey.press(character)
                typeKey.release(character)
                time.sleep(0.005)
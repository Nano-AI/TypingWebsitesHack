import random
import string
import time

import keyboard as kb
from pynput.keyboard import Controller, Key
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

while True:
    intext = input("Hit enter to get ready. (Or type p and hit enter for pass)")
    if intext != "p":
        driver.get('https://play.typeracer.com/')
    input("Hit enter once page is loaded")
    sleep = 0.00025
    # sleep = float(input('Enter time sleep'))
    sleepHalf = sleep / 2
    words = driver.find_elements_by_css_selector('table.inputPanel')
    # print(words[0].text)
    print(f"Press enter to start")
    time.sleep(1)
    typeKey = Controller()
    while not kb.is_pressed('enter'):
        time.sleep(0.01)
    for word in words:
        print(word.text)
        for character in word.text:
            if random.randint(0, 10) <= 1:
                print("typo")
                for x in range(random.randint(1, 2)):
                    typeKey.press(random.choice(string.ascii_letters))
                    time.sleep(sleepHalf)
                    typeKey.release(random.choice(string.ascii_letters))
                    time.sleep(sleepHalf)
                    typeKey.press(Key.backspace)
                    typeKey.release(Key.backspace)
            typeKey.press(character)
            typeKey.release(character)
            time.sleep(sleep)

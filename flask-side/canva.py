from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import json
import random
import pyautogui
import undetected_chromedriver as uc




# Create Chrome options with incognito mode
chrome_options = Options()
#chrome_options.add_argument("--incognito")


with open('credentials.json') as f:
    config = json.load(f)


#if we're already logged in we don't need to do username/pw
username = config['username']
password = config['password']
driver = webdriver.Chrome(options=chrome_options)
def getToCanvaHomepage():
    try:
        getToCanva()
        login()
        
        #if we're not logged in we should call login()


        template_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Templates"]'))
        )
        template_btn.click()



        time.sleep(300)

    finally:
        # Close the browser
        driver.quit()



def login():
    try:
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Log in"]'))
        )
        login_btn.click()
        time.sleep(random.uniform(1,2))
        
        login_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="Continue with Google"]'))
        )
        login_btn.click()

        time.sleep(300)

        time.sleep(random.uniform(1,2))

        for char in username:
            pyautogui.press(char)
            pyautogui.PAUSE(random.uniform(0.2,0.5))
        time.sleep(random.uniform(0.1,0.5))
        pyautogui.press('enter')

        for char in password:
            pyautogui.press(char)
            pyautogui.PAUSE(random.uniform(0.2,0.5))
        time.sleep(random.uniform(0.1,0.5))
        pyautogui.press('enter')
        time.sleep(random.uniform(0.1,0.5))

        continue_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[text()="Continue"]'))
        )



        time.sleep(300)

    finally:
        # Close the browser
        driver.quit()

def getToCanva():
    driver.maximize_window()
    driver.get('https://www.canva.com')
    time.sleep(random.uniform(1,2))

if __name__ == "__main__":
    getToCanvaHomepage()

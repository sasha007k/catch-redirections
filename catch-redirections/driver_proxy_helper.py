import time
from threading import Thread
import pyautogui
import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def enter_proxy_auth(proxy_username, proxy_password):
    time.sleep(1)
    pyautogui.typewrite(proxy_username)
    pyautogui.press('tab')
    pyautogui.typewrite(proxy_password)
    pyautogui.press('enter')

def open_a_page(driver, url):
    driver.get(url)

def create_webdriver_and_input_proxy_credentials():
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server={}'.format(os.getenv('PROXY_HOST') + ":" + os.getenv('PROXY_PORT')))

    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                            options=chrome_options,
                            desired_capabilities=capabilities)

    Thread(target=open_a_page, args=(driver, "http://www.google.com/")).start()
    Thread(target=enter_proxy_auth, args=(os.getenv('PROXY_USERNAME'), os.getenv('PROXY_PASSWORD'))).start()
    time.sleep(3)
    return driver

def create_webdriver_and_clean_logs():
    driver = create_webdriver_and_input_proxy_credentials()
    driver.get_log("performance")
    return driver

import time
from selenium.webdriver.support.ui import WebDriverWait
import url_helper
from selenium.webdriver.common.by import By

def apply_button_on_talent_website(driver):
    time.sleep(2)
    try:
        apply_button = driver.find_elements_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/button[2]')[0]
        if apply_button is not None and apply_button.text.lower() == "apply on company website":
            try:
                apply_button.click()
            except:
                return False
            time.sleep(2)
            skip_button = driver.find_elements_by_xpath('//*[@id="popupBackground"]/div/form/button[2]')[0]
            if skip_button is not None:
                skip_button.click()
                time.sleep(8)
                return True
    except:
        return False
    return False

def apply_button_on_jobs2careers_website(driver):
    time.sleep(2)
    try:
        skip_button = driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div/div/form/p/button')[0]
        if skip_button is not None:
            try:
                skip_button.click()
                time.sleep(3)
                apply_button = driver.find_elements_by_xpath('/html/body/main/div[1]/div/div/div[2]/div/div/div[1]/div[3]/div/button')[0]
                if apply_button is not None and apply_button.text.lower() == "apply":
                    apply_button.click()
                    time.sleep(3)
                    return True
                return False
            except Exception as e:
                return False
    except Exception as e:
        return False

    return False

def apply_button_on_myjobhelper_website(driver):
    time.sleep(1)
    try:
        try:
            apply_button = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[3]/a[1]')[0]
        except:
            apply_button = driver.find_elements_by_xpath('/html/body/div[2]/div[5]/div[2]/a[1]')[0]
        apply_link = apply_button.get_attribute('href')
        if apply_button is None or apply_link is None:
            return False

        driver.get(apply_link)
        wait = WebDriverWait(driver, 20)
        wait.until(lambda driver: url_helper.wait_for_all_redirects_finished(driver))

        return True
    except Exception as e:
        return False

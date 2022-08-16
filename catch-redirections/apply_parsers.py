import time

def apply_button_on_talent_website(driver):
    time.sleep(2)
    try:
        apply_button = driver.find_elements_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div[2]/button[2]')[0]
    except:
        return False
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

    return False

def apply_button_on_jobs2careers_website(driver):
    time.sleep(2)
    try:
        skip_button = driver.find_elements_by_xpath('/html/body/div[4]/div[3]/div/div/form/p/button')[0]
    except Exception as e:
        return False
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

    return False

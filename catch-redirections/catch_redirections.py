import csv
import time
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import random

import driver_proxy_helper
import logs_helper
import apply_parsers
import url_helper


load_dotenv()

jobs_file = open(r"C:\Users\HP\Downloads\Telegram Desktop\jobs-test.csv")
job_links = csv.reader(jobs_file)

driver = driver_proxy_helper.create_webdriver_and_clean_logs()

links_with_redirects = []
i = 1
for link in job_links:

    if i % 6 == 0:
        driver.quit()
        time.sleep(3)
        driver = driver_proxy_helper.create_webdriver_and_clean_logs()

    driver.get(link[0])
    #driver.get("https://www.jobs2careers.com/click.php?jid=5b1bbad7083d71ef6d34cac37&ri=97079d9737224413a6b31dcda527dfaa&job_loc=Jersey+City%2CNJ&q=Licensed+Clinical+Psychologist+Relocate+To+Tennessee&spl=AY5qwQCGqAnt73sx%3ANnvSWthFJA%2BDi6o02lJ5DQ%3D%3D%3A96DSRTfjR0yfBFJr77FBqHPkr1t9NFVsdeglv1xiBNkWej8RNNIjCA%2BS8kixwUPIYBGJaQ5RadKQQ3xe87mqgLG2JdgR6D9lzqT4vzcECpnu3za0i3Q2jant7pO2cZKNofexnhTPGxHQIjh7iuw%3D&encrypt=0&l=Brooklyn%2C+NY&query_category_id=560000&clid=&clt=")
    #time.sleep(8)

    wait = WebDriverWait(driver, 20)
    wait.until(lambda driver: url_helper.wait_for_all_redirects_finished(driver))

    logs = driver.get_log("performance")
    redirects = logs_helper.return_main_url_and_redirects(logs)

    if "talent.com" in redirects[-1]:
        isApplyButton = apply_parsers.apply_button_on_talent_website(driver)
        if isApplyButton:            
            logs = driver.get_log("performance")
            redirects.extend(logs_helper.return_main_url_and_redirects(logs))
    elif "jobs2careers.com" in redirects[-1]:
        isApplyButton = apply_parsers.apply_button_on_jobs2careers_website(driver)
        if isApplyButton:            
            logs = driver.get_log("performance")
            redirects.extend(logs_helper.return_main_url_and_redirects(logs))
    elif "myjobhelper.com" in redirects[-1]:
        isApplyButton = apply_parsers.apply_button_on_myjobhelper_website(driver)
        if isApplyButton:            
            logs = driver.get_log("performance")
            redirects.extend(logs_helper.return_main_url_and_redirects(logs))

    redirects = url_helper.url_postprocessing(redirects)
    links_with_redirects.append(redirects)
    print("{0}".format(i))
    i+=1
    time.sleep(random.randint(1, 4))

driver.quit()

longest_list = max(len(elem) for elem in links_with_redirects)

for link in links_with_redirects:
    while len(link) < longest_list:
        link.insert(len(link)-1, "")

header = []
for i in range(longest_list):
    if i == 0:
        header.append("URL")
    elif i == longest_list -1:
        header.append("landing")
    else:
        header.append("redirect")

links_with_redirects.insert(0, header)

with open(r'C:\Users\HP\Desktop\redirect_test.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(links_with_redirects)

print("DONE")

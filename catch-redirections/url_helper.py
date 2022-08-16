import time

def wait_for_all_redirects_finished(driver):
    temp_url = ""
    while temp_url != driver.current_url:
        temp_url = driver.current_url
        time.sleep(2)

    if "jobs2careers.com" in temp_url:
        time.sleep(5)
    return True

def url_postprocessing(redirects):
   processed_redirects = []
   words_for_remove = ["preloadresumeapply", "https://apply.indeed.com/indeedapply/xpc?v=5"]
   for link in redirects:
       if not any(map(link.__contains__, words_for_remove)):
           processed_redirects.append(link)

   if "captcha" in processed_redirects[-1]:
       processed_redirects.append("Captcha Error")
   return processed_redirects

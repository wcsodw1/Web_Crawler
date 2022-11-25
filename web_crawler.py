# python web_crawler.py
# Reference :　https://ithelp.ithome.com.tw/articles/10276797
# Ref2 : https://ithelp.ithome.com.tw/articles/10277885?sc=iThelpR

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.chrome_executable_path = "./chromedriver.exe"
driver = webdriver.Chrome(options=options)


def linkin():
    List_job = []
    # driver.get(
    #     "https://www.google.com/?gws_rd=ssl/")
    # driver.get(
    #     "https://www.linkedin.com/jobs/search?position=1&pageNum=0/")
    # driver.get("https://www.linkedin.com/jobs/search?keywords=machine%20learning&location=%E7%BE%8E%E5%9C%8B&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")
    driver.get("https://www.linkedin.com/jobs/search?keywords=Machine%20Learning&location=%E7%BE%8E%E5%9C%8B&locationId=&geoId=103644278&f_TPR=&f_WT=2&position=1&pageNum=0")
    # 取得標題 :
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
    titles = driver.find_elements(
        By.CLASS_NAME, "base-search-card__title")
    for title in titles:
        job = title.text
        List_job.append(job)
        df = pd.DataFrame(List_job)
        df.to_csv("./Job_List.csv")

    return df


crawler = linkin()

# Close driver
# driver.close()

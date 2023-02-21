from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json
import sys
from time import sleep

def get_detail_by_author(url,num_video):
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(5)

    def scroll_down(loop):
        count = 0
        while (count < loop):
            try:
                height = driver.execute_script("return document.body.scrollHeight")
                time.sleep(1)
                driver.find_element_by_tag_name('body').send_keys(Keys.END)
                count += 1
            except:
                break

    driver.get(f"{url}/videos")

    scroll_down(loop=10)

    videos = driver.find_elements(By.ID, 'dismissible')

    for vid in videos:
        title = vid.find_element(By.ID,'video-title').text
        url = vid.find_element(By.ID,"thumbnail").get_attribute("href")
        obj = {
            "title": title,
            "url": url
        }
        print(obj)


get_detail_by_author('https://www.youtube.com/@yeah1music',1)
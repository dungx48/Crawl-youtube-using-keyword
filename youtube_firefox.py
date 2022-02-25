from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json
from bs4 import BeautifulSoup

option = Options()
option.headless = False

driver = webdriver.Firefox(options=option)
driver.implicitly_wait(5)

base_url = "https://www.youtube.com/"
keyword = "draven thach dau"


# driver.get(f"{base_url}/search?q={keyword}")


def get_channel_detail():

    driver.get(f"{base_url}/search?q={keyword}")
    detail = []
    time.sleep(3)

    all_video = driver.find_elements(By.ID, 'dismissible')
    for video in all_video:
        title = video.find_element_by_css_selector("#title-wrapper.style-scope.ytd-video-renderer h3.title-and-badge.style-scope.ytd-video-renderer a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer yt-formatted-string.style-scope.ytd-video-renderer").text
        # link_video = video.find_element_by_id("img").get_attribute("src")

        # author = video.find_elements_by_css_selector(".text-wrapper style-scope ytd-video-renderer > style-scope ytd-video-renderer > ")
        # link_author = video.find_element_by_class_name("yt-simple-endpoint style-scope yt-formatted-string").get_attribute("src")

    # links = list(dict.fromkeys(map(lambda a: a.get_attribute("href"), all_channel_list)))


    # cname = driver.find_elements_by_css_selector("#text.style-scope.ytd-channel-name")[0].text
    # cDess = driver.find_elements_by_css_selector("#description-container > yt-formatted-string:nth-child(2)").text

    obj = {
        "title: ": title,
        # "link_video: ": link_video,
        # "author: ": author,
        # "link_author: ": link_author
    }
    detail.append(obj)
    print("------------------")

    return detail



if __name__ == "__main__":
    all_channel_details = get_channel_detail()
    print(json.dumps(all_channel_details))

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
import json
import sys
from time import sleep
from pytube import YouTube


def get_channel_detail(keyword, base_url="https://www.youtube.com/"):
    option = Options()
    option.headless = False
    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(5)

    def scroll_down(loop):
        count = 0
        while (count < loop):
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(2)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            count += 1

    driver.get(f"{base_url}/search?q={keyword}")
    data_path = f"{keyword}.json"
    detail = []
    urls = []

    time.sleep(2)

    scroll_down(5)

    all_video = driver.find_elements(By.ID, 'dismissible')
    for video in all_video:
        title = video.find_element_by_css_selector(
            "#title-wrapper.style-scope.ytd-video-renderer h3.title-and-badge.style-scope.ytd-video-renderer a#video-title.yt-simple-endpoint.style-scope.ytd-video-renderer yt-formatted-string.style-scope.ytd-video-renderer").text
        url = video.find_element_by_css_selector(
            "a#thumbnail.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail").get_attribute("href")
        author = video.find_element_by_css_selector(
            "div#dismissible.style-scope.ytd-video-renderer div.text-wrapper.style-scope.ytd-video-renderer div#channel-info.style-scope.ytd-video-renderer ytd-channel-name#channel-name.long-byline.style-scope.ytd-video-renderer div#container.style-scope.ytd-channel-name div#text-container.style-scope.ytd-channel-name yt-formatted-string#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string").text
        url_author = video.find_element_by_css_selector(
            "div#dismissible.style-scope.ytd-video-renderer div.text-wrapper.style-scope.ytd-video-renderer div#channel-info.style-scope.ytd-video-renderer ytd-channel-name#channel-name.long-byline.style-scope.ytd-video-renderer div#container.style-scope.ytd-channel-name div#text-container.style-scope.ytd-channel-name yt-formatted-string#text.style-scope.ytd-channel-name a.yt-simple-endpoint.style-scope.yt-formatted-string").get_attribute(
            "href")

        obj = {
            "title": title,
            "url": url,
            "author": author,
            "url_author": url_author
        }
        detail.append(obj)
        urls.append(url)

    with open(data_path, "w", encoding='utf8') as file_json:
        json.dump(detail, file_json, ensure_ascii=False)

    return detail




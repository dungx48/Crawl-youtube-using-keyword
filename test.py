from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

base_url = "https://www.youtube.com/"
keyword = "viet linh tinh vao day"

driver = webdriver.Firefox()
driver.get(f"{base_url}/search?q={keyword}")


def slow_scroll_page(driver, speed=2):
    current_scroll_position, new_height = 0, 1
    while current_scroll_position <= new_height:
        current_scroll_position += speed
        driver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = driver.execute_script("return document.body.scrollHeight")


def scroll_page(driver):
    SCROLL_PAUSE_TIME = 1

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_down(loop):
    count = 0
    while (count < loop):
        height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(1)
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        count += 1
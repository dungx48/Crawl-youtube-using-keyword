from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox(executable_path='geckodriver.exe')

browser.get("https://www.facebook.com/")

sleep(3)
# dang nhap
txt_user = browser.find_element_by_id("email")
txt_user.send_keys("vietviet48")

txt_pass = browser.find_element_by_id("pass")
txt_pass.send_keys("Abcd1234.")

#submit
txt_pass.send_keys(Keys.ENTER)

sleep(5)

browser.get("https://www.facebook.com/LienMinhHuyenThoai/photos/a.300395500044704/4387365104681036/")

sleep(3)

cmt_options = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[4]/div[1]/div/div/span")
cmt_options.click()

sleep(2)

choose_full_cmt = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/div/div[3]")
choose_full_cmt.click()

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

sleep(2)

show_more_cmt = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[4]/div[2]/div[1]/div[2]/span/span")
print("1")
show_more_cmt.click()
# sleep(2)

# cmt_list = browser.find_elements_by_xpath("")
# div_cmt = browser.find_elements_by_xpath("//*[@id='mount_0_0_Xf']/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[4]/ul/li[52]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/span/div/div")
# print(div_cmt)
#
# sleep(5)
# browser.close()
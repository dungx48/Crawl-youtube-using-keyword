from selenium import webdriver
from bs4 import BeautifulSoup

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    soup = BeautifulSoup(content)

main()
from pytube import YouTube
import pafy
import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def download(keyword):
    base_url = "https://www.youtube.com/"

    option = Options()
    option.headless = False

    driver = webdriver.Firefox(options=option)
    driver.implicitly_wait(5)

    urls = []
    i = 0
    def scroll_down(loop):
        count = 0
        while (count < loop):
            height = driver.execute_script("return document.body.scrollHeight")
            time.sleep(2)
            driver.find_element_by_tag_name('body').send_keys(Keys.END)
            count += 1

    def progress(stream, chunk, bytes_remaining):
        filesize = stream.filesize
        current = ((filesize - bytes_remaining) / filesize)
        percent = ('{0:.1f}').format(current * 100)
        progress = int(50 * current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()

    driver.get(f"{base_url}/search?q={keyword}")
    # data_path = f"{keyword}.json"

    time.sleep(2)

    scroll_down(5)

    all_video = driver.find_elements(By.ID, 'dismissible')
    for video in all_video:
        url = video.find_element_by_css_selector(
            "a#thumbnail.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail").get_attribute("href")

        urls.append(url)

    for url in urls:
        ptvideo = YouTube(url, on_progress_callback=progress)
        # ptvideo = YouTube(url)
        my_streams = ptvideo.streams.order_by('resolution').desc()
        try:
            mp4_stream = my_streams.filter(file_extension='mp4', progressive=True, resolution='720p')
            print("Video is being downloaded as '%s.mp4'" % ptvideo.title)
            mp4_stream.first().download(f"Download/{keyword}")
        except:
            print("Error")
            i += 1
    print("Error = ", i)
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import re
import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

from sklearn.preprocessing import LabelEncoder

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get('https://www.youtube.com/results?search_query=%C4%91%E1%BA%A3ng')

user_data = driver.find_elements_by_xpath('//*[@id="video-title"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))

df = pd.DataFrame(columns=['link', 'title', 'description', 'category'])

wait = WebDriverWait(driver,10)
v_category = ""
for x in links:
    try:
        driver.get(x)
    except 'InvalidArgumentException':
        print(x)
    v_id = x.strip('https://www.youtube.com/watch?v=')
    v_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.title yt-formatted-string"))).text
    v_description = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#description yt-formatted-string"))).text
    df.loc[len(df)] = [v_id, v_title, v_description, v_category]

frames = [df]

df_link = pd.DataFrame(columns=["link"])
df_title = pd.DataFrame(columns=["title"])
df_description = pd.DataFrame(columns=["description"])
df_category = pd.DataFrame(columns=["category"])

corpus = []
for i in range(0,1000):
    review = re.sub('[^a-zA-Z]', ' ', df_title[i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)



corpus1 = []
for i in range(0, 1000):
  review = re.sub('[^a-zA-Z]', ' ', df_description[i])
  review = review.lower()
  review = review.split()
  ps = PorterStemmer()
  review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
  review = ' '.join(review)
  corpus1.append(review)

dftitle = pd.DataFrame({'title':corpus})
dfdescription = pd.DataFrame({'description':corpus1})
dfcategory = df_category.apply(LabelEncoder().fit_transform)

df_new = pd.concat([df_link, dftitle, dfdescription, dfcategory], axis=1, join_axes = [df_link.index])
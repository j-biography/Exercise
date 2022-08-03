

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(r"C:\Users\JoUkHyeon\Desktop\Python\chromedriver\chromedriver") # 경로 설정 주의

url = "https://news.naver.com/main/ranking/popularDay.naver"

driver.get(url)
driver.implicitly_wait(3)
html = driver.page_source

news1 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[1]/ul/li[1]/div/a')
news2 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[2]/ul/li[1]/div/a')
news3 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[3]/ul/li[1]/div/a')
news4 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[4]/ul/li[1]/div/a')
news5 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[5]/ul/li[1]/div/a')
news6 = driver.find_elements(By.XPATH, '//*[@id="wrap"]/div[4]/div[2]/div/div[6]/ul/li[1]/div/a')


for i in news1 :
    title = i.text
    print(title)

for i in news2 :
    title = i.text
    print(title)

for i in news3 :
    title = i.text
    print(title)

for i in news4 :
    title = i.text
    print(title)

for i in news5 :
    title = i.text
    print(title)

for i in news6 :
    title = i.text
    print(title)


driver.close()
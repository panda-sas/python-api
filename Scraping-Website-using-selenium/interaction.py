from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\Saswati Panda\Development\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get(
    "https://en.wikipedia.org/wiki/Main_Page")

total_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(total_articles.text)
# total_articles.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)


driver.quit()
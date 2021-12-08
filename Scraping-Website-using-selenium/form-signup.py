from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\Saswati Panda\Development\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.get("http://secure-retreat-92358.herokuapp.com/")


f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Sas")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Pan")

l_name = driver.find_element(By.NAME, "email")
l_name.send_keys("panda@home.com")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()

# driver.quit()
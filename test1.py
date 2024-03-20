from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


PATH = r'C:\Program Files (x86)\chromedriver.exe'

service = Service(executable_path=PATH)

options = webdriver.ChromeOptions()
options.add_argument("--headless") 

driver = webdriver.Chrome(service=service, options=options)

url = input("Enter the website URL: ")

driver.get(url)

time.sleep(5)

title = driver.title
print("Title:", title)

second_div = driver.find_element(By.XPATH, "//div[@class='problem-statement']/div[2]")

print(second_div.text)


driver.quit()
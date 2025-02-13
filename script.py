from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path="/home/mohan/Desktop/whatsapp_automation/chromedriver")
driver=webdriver.Chrome(service=service)

driver.get("https://google.com")

time.sleep(10)
driver.quit()
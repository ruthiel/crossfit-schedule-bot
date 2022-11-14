from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = '~/usr/local/bin/chromedriver'
driver = webdriver.Chrome(executable_path=PATH)

driver.get('https://1fight.sportstudio.pt/')
print(driver.title)

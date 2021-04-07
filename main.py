import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.gamestop.com/")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("ps5")
search.send_keys(Keys.RETURN)

print(driver.page_source)

time.sleep(5)

driver.quit()

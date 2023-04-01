from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import requests

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://landing.simetrik.com/esp")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    url = link.get_attribute("href")
    if url is not None and urlparse(url).scheme in ['http', 'https']:
        response = requests.head(url)
        if response.status_code >= 400:
            print(url + " -> is a broken link!" + " -> status code: " + str(response.status_code))


driver.quit()

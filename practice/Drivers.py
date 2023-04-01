import time
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")
firefox_options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'

browsers = {
    "chrome": {"driver": webdriver.Chrome, "options": chrome_options},
    "firefox": {"driver": webdriver.Firefox, "options": firefox_options}
}

browser_name = "chrome"

driver = browsers[browser_name]["driver"](options=browsers[browser_name]["options"])

driver.get("https://www.google.com")
time.sleep(2)

driver.quit()
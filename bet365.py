import chromedriver_autoinstaller as chromedriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import getpass
import pandas as pd

chromedriver.install()

username = getpass.getuser()
options = Options()
web = f'''https://www.bet365.com/#/HO/'''
username = getpass.getuser()
driver = webdriver.Chrome(options=options)
driver.get(web)

time.sleep(10)
inspect = '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div[1]/div[2]/div[2]'
element = driver.find_element('xpath',f'{inspect}')
html_element = element.get_attribute('outerHTML')

with open("./text.html", "w") as f:
    f.write(html_element)

soup = BeautifulSoup(html_element, 'html.parser')
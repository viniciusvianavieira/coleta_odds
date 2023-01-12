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
# options.headless = True
# options.add_argument('window-size=1920x1080') 

web = '''https://sports.sportingbet.com/pt-br/sports/futebol-4'''

username = getpass.getuser()
driver = webdriver.Chrome(options=options)
driver.get(web) 

time.sleep(10)
inspect = '//*[@id="main-view"]/ms-widget-layout/ms-widget-slot[3]/ms-tabbed-grid-widget'
element = driver.find_element('xpath',f'{inspect}')
html_element = element.get_attribute('outerHTML')
print(html_element)
soup = BeautifulSoup(html_element, 'html.parser')
tag = soup.find("ms-event-group")
tag2 = tag.find("ms-event")

participante = tag2.find_all("div", {"class":"participant"})

print(participante[0].contents[0].text)
print(participante[0].contents[1].text)

print(participante[1].contents[0].text)
print(participante[1].contents[1].text)

situacao = tag2.find_all("i", {"class":"live-icon"})

print(situacao[0].contents[0].text)

tempo = tag2.find_all("ms-live-timer")
print(tempo[0].contents[0])

resultado = tag2.find_all("div",{"class":"value-slider--hidden"})
print(resultado[0].contents[0].text)
print(resultado[1].contents[0].text)

choices = tag2.find("ms-group-header",{"class":"grid-group ng-star-inserted"})
print(choices)


odds2 = tag2.find_all("div",{"class":"option option-value"})
print(odds2[0].contents[0].text)
print(odds2[1].contents[0].text)
print(odds2[2].contents[0].text)
print(odds2[3].contents[0].text)
print(odds2[4].contents[0].text)


header = tag2.find_all("div",{"class":"option active ng-star-inserted"})
print(header)


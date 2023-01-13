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
web = f'''https://br.betano.com/live/'''
username = getpass.getuser()
driver = webdriver.Chrome(options=options)
driver.get(web)

time.sleep(10)
inspect = '/html/body/div[1]/div/section[2]/div[5]/div[2]/div/div/div[3]/div'
element = driver.find_element('xpath', f'{inspect}')

html_element = element.get_attribute('outerHTML')

soup = BeautifulSoup(html_element, 'html.parser')

header = soup.find("div", {
                   "class": "live-events-league__header live-events-league__header--clickable"})

body = soup.find_all("div", {
                     "class": "live-events-event-row__container live-event live-events-event-row__container--row"})

# with open("./text.html", "w") as f:
#     f.write(str(body))

for data in body:
    participantes = data.find_all(
        "span", {"class": "live-event__participants__participant-name"})
    print(participantes[0].text)
    print(participantes[1].text)


# cont = 0
# for respostas in body:
#     print("*"*30)
#     print(respostas.find_all("div", {
#         "class": "live-events-league__header live-events-league__header--clickable"}))
#     print("*"*30)

# participants = body.find_all("span",{"class":"live-event__participants__participant-name"})[0]
# odds = body.find_all("span",{"class":"selections__selection__odd"})
# print(odds[0].text)
# print(odds[1].text)
# print(odds[2].text)

# result = body.find_all("span",{"class":"live-event__scores__score__text"})
# print(result[0].text)
# print(result[1].text)

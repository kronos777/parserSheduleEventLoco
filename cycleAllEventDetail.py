import json
from bs4 import BeautifulSoup as bs
from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def getDetailEventInfo(pageHtml, season):
    seasonEvent = season
    dateTimeEvent = ""
    placeEvent = ""
    typeСompetition = ""
    stageСompetition = ""
    commandOne = ""
    commandOneScore = ""
    commandOneLogo = ""
    commandOneCity = ""





driver = webdriver.Firefox()
driver.maximize_window()
url = "https://www.fclm.ru/schedule/7918/"
driver.get(url)
time.sleep(3)


"""
file = open('allFootballEvent.json', encoding="utf8")
data = json.load(file)
#testPlayer = []
for idx, items in enumerate(data):
    for ids, item in enumerate(items):
        print("https://www.fclm.ru" + item)
        break
    break
"""
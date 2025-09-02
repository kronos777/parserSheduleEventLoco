import json
from distutils.command.check import check

import parserDetailEventPage
from bs4 import BeautifulSoup as bs
from click import command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


"""
https://www.fclm.ru/schedule/12158/
"""

driver = webdriver.Firefox()
driver.maximize_window()
file = open('allFootballEvent.json', encoding="utf8")
data = json.load(file)
#testPlayer = []
for idx, items in enumerate(data):
    for ids, item in enumerate(items):
        season = items[0]
        if ids == 0:
            continue
        url = "https://www.fclm.ru" + item
        #url = "https://www.fclm.ru/schedule/12181/"
        checkUrl = url.split('schedule')
        if len(checkUrl) > 0:
            driver.get(url)
            driver.implicitly_wait(5)
            htmlPage = driver.page_source
            soup = bs(htmlPage)
            dataEvent = parserDetailEventPage.parserDetailEventPage().getDetailEventInfo(soup, season)
            prepareData = parserDetailEventPage.parserDetailEventPage().prepareGameForWriteFile(dataEvent)
            parserDetailEventPage.parserDetailEventPage().dump_json(prepareData, 'allFootballEventDetail')
            print(season)
            print(url)
            time.sleep(3)
        #break
    #break
driver.close()
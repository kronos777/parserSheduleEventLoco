import json
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time





file = open('allFootballEvent.json', encoding="utf8")
data = json.load(file)
#testPlayer = []
for idx, items in enumerate(data):
    for ids, item in enumerate(items):
        print(item)
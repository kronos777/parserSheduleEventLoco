import json
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import parserListEventPage


driver = webdriver.Firefox()
driver.maximize_window()
for season in range(1,18):
    url = "https://www.fclm.ru/schedule/"
    driver.get(url)
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, 0);")

    dropdown_trigger = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div")
    dropdown_trigger.click()

    time.sleep(1)

    ul_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div/div/ul")
    li_elements = ul_element.find_elements(By.TAG_NAME, "li")


    for index, li in  enumerate(li_elements):
        if (index == 0 and season == 1):
            htmlPage = driver.page_source
            soup = bs(htmlPage)
            parserListEventPage.parserListEventPage().cycleListLink(soup)
            continue
        if (index == season):
            print(season)
            li.click()
            time.sleep(5)
            htmlPage = driver.page_source
            soup = bs(htmlPage)
            parserListEventPage.parserListEventPage().cycleListLink(soup)
            break





"""
ul_element = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div[1]/form/div[2]/div/div/div/ul")
li_elements = ul_element.find_elements(By.TAG_NAME, "li")
for index, li in  enumerate(li_elements):
        # Example: Get the text of the li element
        if(index == 0):
            continue
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(li)
        )
        element.click()
        #li.click()
        time.sleep(3)
        #li_text = li.text
        #print(f"Li text: {li_text}")
select_element = driver.find_element(By.NAME, "season")
select = Select(select_element)
for index in range(1, 100):
    select.select_by_index(index)
    time.sleep(3)
"""
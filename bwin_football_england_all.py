from queue import Empty
from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Firefox(GeckoDriverManager().install())

driver.get('https://sports.bwin.be/nl/sports/voetbal-4/wedden/engeland-14')

# grids = driver.find_elements_by_css_selector("div.grid-event-wrapper")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.grid-event-wrapper"))
    )

    names = WebDriverWait(element, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.participant"))
    )

    # names = element.find_elements_by_css_selector("div.participant")
    for name in names:
        name = name.text.strip()
        if(len(name) != 0):
            print(name)
finally:
    driver.quit()


# for grid in grids:
#     names = driver.find_elements_by_css_selector("div.participant")
#     for name in names:
#         name = name.text.strip()
#         if(len(name) != 0):
#             print(name)
#     odds = driver.find_elements_by_css_selector("div.option option-value ng-star-inserted")
#     for odd in odds:
#         odd = odd.text.strip()
#         if(len(odd) != 0):
#             print(odd)

driver.close()
driver.quit()
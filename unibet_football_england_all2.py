from queue import Empty
from bs4 import BeautifulSoup
import requests
import re
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://nl-sports.unibet.be/betting/sports/filter/football/england/all/matches')

# ----------------------------------    click on live button   --------------------------------------

# visible = False

# while not visible:
#     try:
#         button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class = "_80525 _35d20"]')))
#         button.click()
#         visible = True
#     except (ElementClickInterceptedException) as e:
#         visible = False

# ------------------------------------    proberen drop down aan te clicken   --------------------------------------


# search = driver.find_element_by_css_selector("div._1490e")

# print(search.text)
# search.click()

# ---------------------------------------   main data ophalen   ---------------------------------------------

games = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_0dfcf"]')))

allOdds = []
allNames = []

for game in games:
    names = WebDriverWait(game, 10).until(EC.presence_of_all_elements_located((By.XPATH, './/div[@class="af24c"]')))
    # names = game.find_elements_by_xpath('.//div[@class="af24c"]')
    for name in names:
        name = name.text.strip()
        if(len(name) != 0):
            print(name)
            allNames.append(name)

    odds = WebDriverWait(game, 10).until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class = "_5a5c0"]')))
    # odds = game.find_elements_by_xpath('.//span[@class = "_5a5c0"]')
    for odd in odds:
        odd = odd.text.strip()
        if(len(odd) != 0):
            print(odd)
            allOdds.append(odd)


print(allOdds)
print(allNames)


time.sleep(5)


driver.close()
driver.quit()

# --------------------   use headers so program don't think you're a bot with beautifulsoup4  -------------------

# page_text = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
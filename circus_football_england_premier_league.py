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
from csv import writer

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://sport.circus.be/nl/sport/sportweddenschappen/844/54210798')


# ----------------------------------    accept cookies  -------------------------------------------

visible = False

while not visible:
    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
        button.click()
        visible = True
    except (ElementClickInterceptedException) as e:
        visible = False


# ----------------------------------    open others competitions  -------------------------------------------

# visible = False

# while not visible:
#     try:
#         buttons = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@role="button"]')))
#         #for button in buttons:
#         #driver.execute_script("arguments[0].click();", buttons)
#         visible = True
#     except (ElementClickInterceptedException) as e:
#         visible = False

# ------------------------------------    proberen drop down aan te clicken   --------------------------------------


# search = driver.find_element_by_css_selector("div._1490e")

# print(search.text)
# search.click()

# ---------------------------------------   main data ophalen   ---------------------------------------------

time.sleep(2)

games = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="bet-event-main-row"]')))

home_team_wins = []
away_team_wins = []
draw = []
home_teams = []
away_teams = []

for game in games:

    names = WebDriverWait(driver = game, timeout = 10).until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class="text"]')))
    if len(names) ==2:
        for i, name in enumerate(names):
            name = name.text.strip()
            if(len(name) != 0):
                print(name)
                if(i % 2 == 0):
                    home_teams.append(name)
                else:
                    away_teams.append(name)


    odds = WebDriverWait(driver = game, timeout = 10).until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class="odd"]')))
    for i in range(3):
        odd = odds[i].text.strip()
        if(len(odd) != 0):
            print(odd)
            if(i % 3 == 0):
                home_team_wins.append(odd)
            elif(i % 2 == 0):
                away_team_wins.append(odd)
            else:
                draw.append(odd)

print(home_teams)
print(len(home_teams))
print('*'*50)
print(away_teams)
print(len(away_teams))
print('*'*50)
print(home_team_wins)
print(len(home_team_wins))
print('*'*50)
print(draw)
print(len(draw))
print('*'*50)
print(away_team_wins)
print(len(away_team_wins))


# -----------------------------------   write to csv file   --------------------------------------------

# with open('unibet_football_england_premier_league.csv', 'w', encoding='utf8', newline='') as f:
#     thewriter = writer(f)
#     header = ['Home_team', 'Away_team', 'Home_team_win', 'Draw', 'Away_team_win']
#     thewriter.writerow(header)

#     for i in range(19):
#         line = [home_teams[i], away_teams[i], home_team_wins[i], draw[i], away_team_wins[i]]
#         thewriter.writerow(line)


driver.close()
driver.quit()

# --------------------   use headers so program don't think you're a bot with beautifulsoup4  -------------------

# page_text = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
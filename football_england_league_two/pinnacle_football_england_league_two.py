import re
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from csv import writer

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.pinnacle.com/en/soccer/england-league-2/matchups#period:0')

print("/"*100)
print("PINNACLE")
print("/"*100)

# ----------------------------------    accept cookies  -------------------------------------------

# visible = False

# while not visible:
#     try:
#         button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
#         button.click()
#         visible = True
#     except (ElementClickInterceptedException) as e:
#         visible = False
#     except (TimeoutException) as t:
#         visible = True

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

# ---------------------------------------   main data ophalen   ---------------------------------------------

time.sleep(2)

games = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="style_row__3q4g_ style_row__3hCMX"]')))

print(len(games))

home_team_wins = []
away_team_wins = []
draw = []
home_teams = []
away_teams = []

for game in games:
    try:
        names = WebDriverWait(driver = game, timeout = 10).until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class="ellipsis event-row-participant style_participant__H8-ku"]')))
        print(len(names))
        odds = WebDriverWait(driver = game, timeout = 10).until(EC.presence_of_all_elements_located((By.XPATH, './/span[@class="style_price__15SlF"]')))
        print(len(odds))
        if len(names) == 2 and len(odds) >= 3:
            for i, name in enumerate(names):
                name = name.text.strip()
                if(len(name) != 0):
                    # print(name)
                    if(i % 2 == 0):
                        home_teams.append(name)
                    else:
                        away_teams.append(name)

            
            for i in range(3):
                odd = odds[i].text.strip()
                if(len(odd) != 0):
                    # print(odd)
                    if(i % 3 == 0):
                        home_team_wins.append(odd)
                    elif(i % 2 == 0):
                        away_team_wins.append(odd)
                    else:
                        draw.append(odd)
    except (TimeoutException) as t:
        continue

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

with open('.\\football_england_league_two\\pinnacle_football_england_league_two.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Home_team', 'Away_team', 'Home_team_win', 'Draw', 'Away_team_win']
    thewriter.writerow(header)

    for i in  range(len(home_teams)):
        line = [home_teams[i], away_teams[i], home_team_wins[i], draw[i], away_team_wins[i]]
        thewriter.writerow(line)


driver.close()
driver.quit()

# --------------------   use headers so program don't think you're a bot with beautifulsoup4  -------------------

# page_text = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
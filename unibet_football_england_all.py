from queue import Empty
from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://nl-sports.unibet.be/betting/sports/filter/football/england/all/matches')

# games = driver.find_elements_by_class_name("a9753 _24efa _8f2c1") # _4a05b
# allOdds = []
# allNames = []

# for game in games:
#     names = game.find_elements_by_class_name("af24c")
#     for name in names:
#         name = name.text.strip()
#         if(len(name) != 0):
#             print(name)
#             allNames.append(name)

#     odds = game.find_elements_by_xpath('.//span[@class = "_5a5c0"]')
#     for odd in odds:
#         odd = odd.text.strip()
#         if(len(odd) != 0):
#             print(odd)
#             allOdds.append(odd)


# print(allOdds)
# print(allNames)

allNames = []

names = driver.find_elements_by_class_name("af24c")
for name in names:
        name = name.text.strip()
        if(len(name) != 0):
            print(name)
            allNames.append(name)
print(allNames)

driver.close()
driver.quit()






# url = 'https://nl-sports.unibet.be/betting/sports/filter/football/england/all/matches'
# page_text = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text

# soup = BeautifulSoup(page_text, 'lxml')

# games = soup.find_all('div', class_ = 'fa117')

# print(games)

# print(soup.find_all("div", string=re.compile("Kameroen")))


""" html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
games = soup.find_all('div')
print(games) """





    
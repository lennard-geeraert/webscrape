from queue import Empty
from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://nl-sports.unibet.be/betting/sports/filter/football/england/all/matches')

names = driver.find_elements_by_class_name("af24c")

for n in names:
    n = n.text.strip()
    if(len(n) != 0):
        print(n)

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





    
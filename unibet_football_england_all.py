from queue import Empty
from bs4 import BeautifulSoup
import requests
import re

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://nl-sports.unibet.be/betting/sports/filter/football/england/the_championship/all/matches')

driver.find_element_by_xpath("//div[@class='a4f9b']/span[@class='e517e' and text()='Totaal doelpunten']").click() 
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@class='a4f9b']/span[@class='e517e' and text()='Totaal doelpunten']"))).click()
#WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='e517e' and text()='Totaal doelpunten']/span[text()='Totaal doelpunten']"))).click()
#driver.find_element_by_xpath("//div[@class='a4f9b']/span[text()='Totaal doelpunten']").click() 
#driver.find_element_by_xpath("//div[@class='a4f9b' and @role='menuItem' and .='Totaal doelpunten']").click()
#driver.find_element_by_xpath("//div[@class='a4f9b']/span[@class='e517e']").click()
#driver.find_element_by_xpath("//div[@class='a4f9b']/span[@class='e517e']")[2].text.click()
games = driver.find_elements_by_class_name("_0dfcf") # _4a05b _0dfcf f10e9
print(games[0])

allOdds = []
allNames = []

for game in games:
    names = game.find_elements_by_class_name("af24c")
    for name in names:
        name = name.text.strip()
        if(len(name) != 0):
            print(name)
            allNames.append(name)

    odds = game.find_elements_by_xpath('.//span[@class = "_5a5c0"]')
    for odd in odds:
        odd = odd.text.strip()
        if(len(odd) != 0):
            print(odd)
            allOdds.append(odd)


print(allOdds)
print(allNames)

# allNames = []

# names = driver.find_elements_by_class_name("af24c")
# for name in names:
#         name = name.text.strip()
#         if(len(name) != 0):
#             print(name)
#             allNames.append(name)
# print(allNames)

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





    
import time

import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 "
                  "Safari/537.36"
}

url = "https://search-intelligence.co.uk/niche-finder/"
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
time.sleep(10)

data = []
import csv
while True:
    mytable = driver.find_element(By.ID, 'example')
    for row in mytable.find_elements(By.CSS_SELECTOR,'tr'):
        for cell in row.find_elements(By.CSS_SELECTOR,'td'):
            print(cell.text)
            data.append(cell.text)
        if len(data) > 0:
            with open("niche_finder.csv", "a", encoding='utf-8') as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(data)
        data.clear()

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, 'example_next').click()
    time.sleep(10)

#
# soup = BeautifulSoup(requests.get(url, headers=headers).text, 'lxml')
# table = soup.find('table', attrs={'id':'example'})
# print(table.text)

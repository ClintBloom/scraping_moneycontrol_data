## double hash mark is for debugging

from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

url_active_calls = 'https://www.investing.com/indices/indices-futures'

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
time_to_sleep = 60


def investing_pages() -> list:

    table_content = []
    driver.get(url_active_calls)
    sleep(time_to_sleep)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('investing.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all(class_='datatable_body__cs8vJ')

    for x in range(3):

        title_content = table[x].find_all('tr')

        for i in range(len(title_content)):

            data = title_content[i].find_all('td')
            title = title_content[i].a.text
            last = data[3].text
            high = data[4].text
            low = data[5].text
            chg = data[6].text
            change_percent = data[7].text
            time_stamp = data[8].text
            table_content.append([title,
                                  last,
                                  high,
                                  low,
                                  chg,
                                  change_percent,
                                  time_stamp])
    return table_content


def close_driver():
    driver.quit()

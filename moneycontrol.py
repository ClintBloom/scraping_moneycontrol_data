## double hash mark is for debugging

from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep


url_active_calls = 'https://www.moneycontrol.com/stocks/fno/marketstats/options' \
                   '/active_calls/homebody.php?opttopic=active%20calls&optinst' \
                   '=allopt&sel_mth=1&sort_order=0'

url_active_puts = 'https://www.moneycontrol.com/stocks/fno/marketstats/options' \
                  '/active_puts/homebody.php?opttopic=active%20puts&optinst' \
                  '=allopt&sel_mth=1&sort_order=0'

url_gainers = 'https://www.moneycontrol.com/stocks/fno/' \
              'marketstats/futures/gainers/homebody.php'

urL_losers = 'https://www.moneycontrol.com/stocks/fno/' \
             'marketstats/futures/losers/homebody.php'

url_indices = 'https://www.moneycontrol.com/markets/' \
              'indian-indices/top-nse-50-companies-list/' \
              '9?classic=true&categoryId=1&exType=N'

url_news = 'https://www.moneycontrol.com/markets/fno-market-snapshot'


# Selenium setup
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)
time_to_sleep = 60


def moneycontrol_active_calls() -> list:

    table_content = []
    driver.get(url_active_calls)
    sleep(time_to_sleep) # Allow loading of dynamic page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('active_call.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all(class_='TAL')

    for sym in table:

        title = sym.text
        content = sym.find_next_siblings('td')
        change_full = str(content[4].find('span')).split('>')
        change_number = change_full[1][:-4]
        change_percent = change_full[2][:-6]

        high_low = str(content[5]).split('<br/>')
        high = high_low[0][4:]
        low = high_low[1][:-5]

        open_int_change = str(content[10].find('span')).split('>')
        open_number = open_int_change[1][:-4]
        open_change_num = open_int_change[2][:-6]

        table_content.append([title,
                              content[0].text,
                              content[1].text,
                              content[2].text,
                              content[3].text,
                              [change_number, change_percent],
                              [high, low],
                              content[6].text,
                              content[7].text,
                              content[8].text,
                              content[9].text,
                              [open_number, open_change_num]])
    return table_content


def moneycontrol_active_puts() -> list:

    table_content = []
    driver.get(url_active_puts)
    sleep(time_to_sleep) # Allow loading of dynamic page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('active_puts.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all(class_='TAL')

    for sym in table:

        title = sym.text
        content = sym.find_next_siblings('td')
        change_full = str(content[4].find('span')).split('>')
        change_number = change_full[1][:-4]
        change_percent = change_full[2][:-6]

        high_low = str(content[5]).split('<br/>')
        high = high_low[0][4:]
        low = high_low[1][:-5]

        open_int_change = str(content[10].find('span')).split('>')
        open_number = open_int_change[1][:-4]
        open_change_num = open_int_change[2][:-6]

        table_content.append([title,
                              content[0].text,
                              content[1].text,
                              content[2].text,
                              content[3].text,
                              [change_number, change_percent],
                              [high, low],
                              content[6].text,
                              content[7].text,
                              content[8].text,
                              content[9].text,
                              [open_number, open_change_num]])
    return table_content


def moneycontrol_gainers() -> list:

    table_content = []
    driver.get(url_gainers)
    sleep(time_to_sleep) # Allow loading of dynamic page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('gainers.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all(class_='TAL')

    for sym in table:

        title = sym.text
        content = sym.find_next_siblings('td')
        change_full = str(content[4].text).split()
        change_number = change_full[0]
        change_percent = change_full[1]

        high_low = content[5].text

        vol_shares_contract = content[6].text.split()
        vol = vol_shares_contract[0]
        shares_contract = vol_shares_contract[1]

        open_int_change = content[9].text.split()
        open_int = open_int_change[0]
        int_change = open_int_change[1]

        table_content.append([title,
                              content[0].text,
                              content[1].text,
                              content[2].text,
                              content[3].text,
                              [change_number, change_percent],
                              high_low,
                              [vol, shares_contract],
                              content[7].text,
                              content[8].text,
                              [open_int, int_change]])
    return table_content


def moneycontrol_losers() -> list:

    table_content = []
    driver.get(urL_losers)
    sleep(time_to_sleep) # Allow loading of dynamic page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('losers.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find_all(class_='TAL')

    for sym in table:

        title = sym.text
        content = sym.find_next_siblings('td')
        change_full = str(content[4].text).split()
        change_number = change_full[0]
        change_percent = change_full[1]

        high_low = content[5].text

        vol_shares_contract = content[6].text.split()
        vol = vol_shares_contract[0]
        shares_contract = vol_shares_contract[1]

        open_int_change = content[9].text.split()
        open_int = open_int_change[0]
        int_change = open_int_change[1]

        table_content.append([title,
                              content[0].text,
                              content[1].text,
                              content[2].text,
                              content[3].text,
                              [change_number, change_percent],
                              high_low,
                              [vol, shares_contract],
                              content[7].text,
                              content[8].text,
                              [open_int, int_change]])
    return table_content


def moneycontrol_indices() -> list:

    table_content = []
    driver.get(url_indices)
    sleep(time_to_sleep) # Allow loading of dynamic page
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('indices.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')

    main_table = soup.find(['table'], {'id': 'indicesTable'})
    table = main_table.tbody
    for tab in table:
        data_text = tab.text.split()
        if data_text:
            data_text.pop()
            if len(data_text) > 8:
                data_text[0] = f'{data_text[0]} {data_text[1]}'
                data_text.pop(1)
                table_content.append(data_text)

    return table_content


def moneycontrol_news() -> list:

    table_content = []
    driver.get(url_news)
    sleep(time_to_sleep)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    ##with open('news.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
    table = soup.find(['div'], {'id': 'news_tab'})
    date = table.find_all('p')
    tags = table.find_all('a')

    for tag in range(len(date)):
        time = date[tag].text[:13]
        title = tags[tag]['title']
        table_content.append([time, title])

    return table_content


def close_driver():
    driver.quit()

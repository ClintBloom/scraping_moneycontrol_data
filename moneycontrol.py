## double hash mark is for debugging

from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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

url_losers = 'https://www.moneycontrol.com/stocks/fno/' \
             'marketstats/futures/losers/homebody.php'

url_indices = 'https://www.moneycontrol.com/markets/' \
              'indian-indices/top-nse-50-companies-list/' \
              '9?classic=true&categoryId=1&exType=N'

url_news = 'https://www.moneycontrol.com/markets/fno-market-snapshot'


# Selenium setup
options = Options()
options.headless = True


class ActiveCalls:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_active_calls)

    def refresh(self):
        self.driver.refresh()

    def moneycontrol_active_calls(self) -> list:

        table_content = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ##with open('active_call.html', 'r', encoding='utf-8') as f:
        ##soup = BeautifulSoup(f, 'lxml')
        table = soup.find_all(class_='TAL')[:140]

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
                                       f'{change_number} / {change_percent}',
                                       f'{high} / {low}',
                                       content[6].text,
                                       content[7].text,
                                       content[8].text,
                                       content[9].text,
                                       f'{open_number} / {open_change_num}'])

        return table_content


class ActivePuts:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_active_puts)

    def refresh(self):
        self.driver.refresh()

    def moneycontrol_active_puts(self) -> list:
        table_content = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ##with open('active_puts.html', 'r', encoding='utf-8') as f:
            ##soup = BeautifulSoup(f, 'lxml')
        table = soup.find_all(class_='TAL')[:140]

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
                                  f'{change_number} / {change_percent}',
                                  f'{high} / {low}',
                                  content[6].text,
                                  content[7].text,
                                  content[8].text,
                                  content[9].text,
                                  f'{open_number} / {open_change_num}'])

        return table_content


class Gainers:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_gainers)

    def refresh(self):
        self.driver.refresh()

    def moneycontrol_gainers(self) -> list:

        table_content = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ##with open('gainers.html', 'r', encoding='utf-8') as f:
            ##soup = BeautifulSoup(f, 'lxml')
        table = soup.find_all(class_='TAL')[:100]

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
                                  f'{change_number} / {change_percent}',
                                  high_low,
                                  f'{vol} / {shares_contract}',
                                  content[7].text,
                                  content[8].text,
                                  f'{open_int} / {int_change}'])

        return table_content


class Losers:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_losers)

    def refresh(self):
        self.driver.refresh()

    def moneycontrol_losers(self) -> list:

        table_content = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ##with open('losers.html', 'r', encoding='utf-8') as f:
            ##soup = BeautifulSoup(f, 'lxml')
        table = soup.find_all(class_='TAL')[:100]

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
                                  f'{change_number} / {change_percent}',
                                  high_low,
                                  f'{vol} / {shares_contract}',
                                  content[7].text,
                                  content[8].text,
                                  f'{open_int} / {int_change}'])

        return table_content


class Indices:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        self.driver.get(url_indices)

    def refresh(self):
        self.driver.refresh()

    def moneycontrol_indices(self) -> list:

        # try:
        #     # Notification Bar exit
        #     print('Notification found and closed')
        #     self.driver.find_element(By.XPATH, '//*[@id="wzrk-cancel"]').click()
        #
        # except NoSuchElementException:
        #     print('Notification not found moving on')
        #
        # sleep(1)
        self.refresh()
        sleep(5)
        try:
            self.driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/span').click()

        except:
            pass

        self.driver.find_element(By.XPATH, '/html/body/section/div/div/ul/li[2]/a/span').click()
        sleep(10)
        table_content = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        ##with open('indices.html', 'r', encoding='utf-8') as f:
            ##soup = BeautifulSoup(f, 'lxml')

        main_table = soup.find(['div'], id='indicesTableDataML')
        table = main_table.find('table')
        table_row = table.find_all('tr')[1:]

        for tab in table_row:
            if tab.text.split():
                table_content.append(tab.text.split())

        return table_content


class News:

    def __init__(self):
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url_news)

    def refresh(self):

        self.driver.refresh()

    def moneycontrol_news(self) -> list:

        table_content = []
        html = self.driver.page_source
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



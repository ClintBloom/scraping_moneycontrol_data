from time import sleep
import moneycontrol
import investing
import googledoc
import datetime

# Time for market, and market close (hour, minutes)
MARKET = datetime.time(9, 15)
MARKET_CLOSE = datetime.time(15, 35)

first_run = True
loading_page = 30 # Time to allow page to load, This is a requirement
time_before_refresh = 270  # How often you want the scraper to run

while 1:

    WEEKDAY = datetime.datetime.weekday(datetime.datetime.utcnow() +
                                        datetime.timedelta(hours=5, minutes=30))
    if WEEKDAY in (1, 2, 3, 4, 5, 6, 7):
        UTC_TO_IST = datetime.datetime.utcnow() + \
                      datetime.timedelta(hours=5, minutes=30)

        if MARKET <= UTC_TO_IST.time() < MARKET_CLOSE:
            print('Running')

            if first_run:
                print('Initializing...')
                calls = moneycontrol.ActiveCalls()
                puts = moneycontrol.ActivePuts()
                gainers = moneycontrol.Gainers()
                losers = moneycontrol.Losers()
                indices = moneycontrol.Indices()
                news = moneycontrol.News()
                investing_page = investing.InvestingPages()
                first_run = False

            else:
                print(f'Starting Scraping, Page Loading - {loading_page} Seconds')
                sleep(loading_page) # time to load page Required for dynamic websites

                googledoc.write_to_file_calls(calls.moneycontrol_active_calls())
                googledoc.write_to_file_puts(puts.moneycontrol_active_puts())
                googledoc.write_to_file_gainers(gainers.moneycontrol_gainers())
                googledoc.write_to_file_losers(losers.moneycontrol_losers())
                googledoc.write_to_file_indices(indices.moneycontrol_indices())
                googledoc.write_to_file_news(news.moneycontrol_news())
                googledoc.write_to_file_investing(investing_page.investing_pages())

                print(f'Waiting {time_before_refresh} Seconds before refresh')
                sleep(time_before_refresh) # time before scraper runs again
                print('Refreshing')

                calls.refresh()
                puts.refresh()
                gainers.refresh()
                losers.refresh()
                indices.refresh()
                news.refresh()
                investing_page.refresh()



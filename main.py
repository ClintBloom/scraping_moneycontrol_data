from time import sleep
import moneycontrol
import investing
import googledoc
import datetime

# Time for market, and market close (hour, minutes)
MARKET = datetime.time(9, 15)
MARKET_CLOSE = datetime.time(15, 35)

while 1:

    WEEKDAY = datetime.datetime.weekday(datetime.datetime.utcnow() + datetime.timedelta(hours=5,minutes=30))
    if WEEKDAY in (1, 2, 3, 4, 5):
        UTC_TO_IST = datetime.datetime.utcnow() + \
                     datetime.timedelta(hours=5, minutes=30)

        if MARKET <= UTC_TO_IST.time() < MARKET_CLOSE:
            googledoc.write_to_file_calls(moneycontrol.moneycontrol_active_calls())
            googledoc.write_to_file_puts(moneycontrol.moneycontrol_active_puts())
            googledoc.write_to_file_gainers(moneycontrol.moneycontrol_gainers())
            googledoc.write_to_file_losers(moneycontrol.moneycontrol_losers())
            googledoc.write_to_file_indices(moneycontrol.moneycontrol_indices())
            googledoc.write_to_file_news(moneycontrol.moneycontrol_news())
            googledoc.write_to_file_investing(investing.investing_pages())

            moneycontrol.close_driver()
            investing.close_driver()
            sleep(300)

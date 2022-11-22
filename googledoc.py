## Double has is for debugging

import gspread


service_account = gspread.service_account(filename='money.json')

spreadsheet = 'Money Control' # spreadsheet name ( filename )
worksheet_name = 'Sheet1' # Sheet1 is default

sheet = service_account.open(spreadsheet)
worksheet = sheet.worksheet(worksheet_name)

seconds_to_wait = 1.5


def write_to_file_calls(data):
    worksheet.update('A1:O141', data)
    print('Calls updated')


def write_to_file_puts(data):
    worksheet.update('A145:O286', data)
    print('Puts updated')

def write_to_file_gainers(data):
    worksheet.update('A290:K391', data)
    print('Gainers updated')

def write_to_file_losers(data):
    worksheet.update('A395:L496', data)
    print('Losers updated')

def write_to_file_indices(data):
    worksheet.update('A500:M550', data)
    print('Indices updated')

def write_to_file_news(data):
    worksheet.update('A555:B565', data)
    print('News updated')

def write_to_file_investing(data):
    worksheet.update('A570:G620', data)
    print('Investing updated')
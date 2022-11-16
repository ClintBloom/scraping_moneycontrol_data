## Double has is for debugging

import gspread


service_account = gspread.service_account()
#service_account = gspread.service_account(filename='keys.json')

spreadsheet = 'kollin' # spreadsheet name ( filename )
worksheet_name = 'Sheet1' # Sheet1 is default

sheet = service_account.open(spreadsheet)
worksheet = sheet.worksheet(worksheet_name)


def write_to_file_calls(data):

    send_column = 1
    for check_row in range(0, 201):
        for i in data[check_row]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row]) + 1:
                send_column = 1


def write_to_file_puts(data):

    send_column = 1
    for check_row in range(203, 404):
        for i in data[check_row - 203]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 203]) + 1:
                send_column = 1


def write_to_file_gainers(data):

    send_column = 1
    for check_row in range(406, 507):
        for i in data[check_row - 406]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 406]) + 1:
                send_column = 1


def write_to_file_losers(data):

    send_column = 1
    for check_row in range(508, 579):
        for i in data[check_row - 508]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 508]) + 1:
                send_column = 1


def write_to_file_indices(data):

    send_column = 1
    for check_row in range(581, 600):
        for i in data[check_row - 581]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 581]) + 1:
                send_column = 1


def write_to_file_news(data):

    send_column = 1
    for check_row in range(601, 611):
        for i in data[check_row - 601]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 601]) + 1:
                send_column = 1


def write_to_file_investing(data):

    send_column = 1
    print(len(data))
    for check_row in range(612, 661):
        for i in data[check_row - 613]:
            #print(check_row + 1, send_column, str(i))
            worksheet.update_cell(check_row + 1, send_column, str(i))
            send_column += 1
            if send_column == len(data[check_row - 613]) + 1:
                send_column = 1